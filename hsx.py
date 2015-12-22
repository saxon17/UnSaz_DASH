import dpkt
import  pandas as pd
import matplotlib.pyplot as plt


def Get_Youtube_IP_DF(PcapDF):
    # print PcapDF.columns()
    IP_Group = PcapDF.groupby('SourceIP')
    # for key,ipGroup in IP_Group:
    #     print key
    #     print ipGroup
    #     print '***************************'


    ip_tcpSum_Seri =  IP_Group.TcpLen.sum()


    # print ip_tcpSum_Seri.index


    YoutubeIP =  ip_tcpSum_Seri[ip_tcpSum_Seri == ip_tcpSum_Seri.max()].index[0]

    PcapDF = PcapDF[PcapDF['SourceIP']== YoutubeIP]
    return PcapDF
def get_first_package_TS(pcap):
    for ts, buf in pcap:
        print ts
        print "over"
        break;
    return  ts
def numIP2strIP(ip):
    '''
    this function convert decimal ip to dot notation
    '''
    l = [str((ip >> 8*n) % 256) for n in range(4)]
    l.reverse()
    return ".".join(l)
def numIP2strIPv6(ip):
    '''
    this function adds ':' to the ipv6 hex address
    '''
    ipv6 = ':'.join([ip[i:i+4] for i in range(0, len(ip), 4)])        
    return ipv6
def block_Dataframe(pcap_file_path):

    # Open Pcap    Then transform Pcap to py__dict__
    f = open(pcap_file_path, 'rb')
    pcap = dpkt.pcap.Reader(f)

    pktCounter = 0
    pktCounter_lst = []
    src_ip_lst = []
    tar_ip_lst = []
    tcp_segment_length_lst = []
    ts_lst = []
    seq_lst = []
    ack_lst = []

    # Read pcap

    # get the time_stamp of the first package

    FirstTS = get_first_package_TS(pcap)


    for ts, buf in pcap:

        pktCounter += 1



        try:
            ether = dpkt.ethernet.Ethernet(buf)
                            
            # Mac address
            smac = ether.src.encode("hex")
            dmac = ether.dst.encode("hex")
            srcmac = ':'.join([smac[i:i+2] for i in range(0, len(smac), 2)])
            dstmac = ':'.join([dmac[i:i+2] for i in range(0, len(dmac), 2)])
            
            # Ports
            tcp = ether.data.data
            srcport = tcp.sport
            dstport = tcp.dport
            
            # Protocol
            prot = ether.data.p
            
            # Packet Size
            sizeP = len(buf)
            
            # Layer 3 Packet
            ethDict = ether.__dict__
            cutBrack = str(ethDict).strip('{))}')
            grablayer = cutBrack.split('data=', 1)[1]
            formatType = grablayer.replace('(', ', ', 1)
            removeDat = formatType.split(', data=', 1)[0]
            
            layertype = removeDat.split(', ', 1)
         
            # # Determine IP type to convert and run proper code
            if ether.type == dpkt.ethernet.ETH_TYPE_IP:
                       
                srcip = numIP2strIP(int(ether.data.src.encode('hex'), 16))
                dstip = numIP2strIP(int(ether.data.dst.encode('hex'), 16))
                Length= ether.data.len

            else:
            
                srcip = numIP2strIPv6(ether.data.src.encode('hex'))
                dstip = numIP2strIPv6(ether.data.dst.encode('hex'))
                Length = ether.ip6.plen
                
            
            
                   
                
                # print type(ether.data.data)
                # print type(tcp.ack)
                # print repr(tcp)
                # print ethDict
            # print pktCounter,srcip,dstip,tcp.ack,tcp.seq,    round(ts - FirstTS , 6 )

            src_ip_lst.append(srcip)
            
            tar_ip_lst.append(dstip)
            tcp_segment_length_lst.append(Length-52)
            if (layertype[0]=='TCP'):
                ack_lst.append(tcp.ack)
            else:
                ack_lst.append(0)
            if (layertype[0]=='TCP'):   
                seq_lst.append(tcp.seq)
            else:
                seq_lst.append(0)

            pktCounter_lst.append(pktCounter)
            ts_lst.append(round(ts - FirstTS , 6 ))


        except AttributeError:
            pass


    d = {'SourceIP' : pd.Series(src_ip_lst, index=range(1,len(src_ip_lst)+1)),
         'TargetIP' : pd.Series(tar_ip_lst, index=range(1,len(tar_ip_lst)+1)),
         'TcpLen':    pd.Series(tcp_segment_length_lst,index=range(1,len(tcp_segment_length_lst)+1)),
         # 'seq':       pd.Series(seq_lst,index=range(1,len(seq_lst)+1)),
         'ack':       pd.Series(ack_lst,index=range(1,len(ack_lst)+1)),
         'Time':      pd.Series(ts_lst,index=range(1,len(ts_lst)+1 )) 
        }
    Pcap_DF = pd.DataFrame(d)

    # Delete package which tcp.len == 0
    Pcap_DF = Pcap_DF[Pcap_DF['TcpLen']>0]

    # print Pcap_DF
    Pcap_DF = Get_Youtube_IP_DF(Pcap_DF)



    gourped = Pcap_DF.groupby('ack')

    # print gourped




    #-----Initial the  Final DataFrame----------------
    tcp_ack_sum_lst = []
    ts_sum_lst = []
    block_ts_start_lst = []
    block_ts_end_lst = []

    df = pd.DataFrame()
    #           })



    # gourp DataFrame with same ACK
    for k,ack_gourp_DF in gourped:
        # TCP Segment sum > 0
            # if k == 347938645 :
            #     print  k
            #     print  ack_gourp_DF
            #     ack_gourp_DF.to_excel("Debug.xls")
            # print '**************************************'


            #Google Video IP Mask --- filter 
            # mask = (ack_gourp_DF.SourceIP == '74.125.102.105')
            # ack_gourp_DF = ack_gourp_DF[mask]



            # Picker
            # Pick first package of every group and caculate the sum    (ack_gourp_DF['TcpLen'].sum())   of each group
            if ack_gourp_DF['TcpLen'].sum() > 100000 :

                ack_gourp_DF_head = ack_gourp_DF.head(1)
                df = pd.concat([df,ack_gourp_DF_head])

                #ack_sum Series
                tcp_ack_sum_lst.append( ack_gourp_DF['TcpLen'].sum())
                ts_sum_lst.append(ack_gourp_DF['Time'].max()-ack_gourp_DF['Time'].min())

                block_ts_start_lst.append(ack_gourp_DF['Time'].min())
                block_ts_end_lst.append(ack_gourp_DF['Time'].max())
                # ack_gourp_DF.to_excel('path_to_file.xlsx', sheet_name='Sheet1',engine='xlsxwriter')
                # f.write(ack_gourp_DF['TcpLen'].sum())
    # print df
    # print 'add:\n'
    # print pd.Series(tcp_ack_sum_lst)
    df['block_size']= pd.Series(tcp_ack_sum_lst,index=df.index)
    df['block_size'] = df['block_size']/1000

    df['block_time'] = pd.Series(ts_sum_lst,index=df.index)

    df['start'] = pd.Series(block_ts_start_lst,index=df.index)
    df['end'] = pd.Series(block_ts_end_lst,index=df.index)


    # print df


    df = df.set_index('ack')

    df2 =  df.drop(['TcpLen','Time','SourceIP','TargetIP'],axis = 1)


    return df2



# file_path_1 = 'aint better than love-0430-360P.pcap'
# file_path_2 = 'aint better than love-0430-720P.pcap'
# file_path_3 = 'aint better than love-0430-1080P.pcap'
# df360P = block_Dataframe(file_path_1) 


# df720P = block_Dataframe(file_path_2)
# df1080P = block_Dataframe(file_path_3)

# print df1080P

# MutiPix =  pd.concat([df360P,df720P,df1080P],axis=1)
# df360P['v'] = df360P['block_size']/df360P['block_time'] 
# df360P.to_excel("720p.xls")
#Rename MutiPix
# MutiPix.columns = ['360p_size','360p_time','720p_size','720p_time','1080p_size','1080p_time']



# MutiPix['1080P'] = df1080P.block_size

# print MutiPix.head(10)
# plt.figure()
# ______________Compare use plot_______bar_________________________________________
# MutiPix['1080p_size'].plot(kind = 'scatter',color = 'r').get_figure()
# MutiPix['720p_size'].plot(kind = 'scatter',color = 'y').get_figure()
# MutiPix['360p_size'].plot(kind = 'scatter',color = 'b').get_figure()

# ______________Compare use plot_______scatter_______________________________________
# df360P.plot(kind = 'scatter' , x ='block_time' , y = 'block_size', s = 50 ,color='DarkGreen' , label = '360P' )
# print type(df720P.plot(kind = 'scatter' , x ='block_size' , y = 'v' ))
# MutiPix.plot(kind = 'scatter' , x ='1080p_size' )
# plt.legend(loc = 'best')
# plt.show()
# plt.savefig('scatter.png')



# print "over"sdsds