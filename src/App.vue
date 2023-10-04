<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'

</script>
<template>
  <el-header>
    Deep Traffic Segmenter
  </el-header>
  <div class="main">





      <RouterView />


    
  </div>
</template>
<script>
export default {

  data() {
    return {
      activeName: 'web',
      currentWebName: '--',
      activeTableName: 'Traffic',
      actionSequenceColorDict: {
        0: "#E7EDF7",
        1: "#D4E4F2",
        2: "#BAD1E6",
        3: "#F7E9E4",
        4: "#E8D0D0"
      },
      currentActionId: null,
      currentActionOne: null,
      webList: [{ name: 'Google' }, { name: 'Github' }, { name: 'Wikipedia' }, { name: 'Faceboook' }, { name: 'Youtube' }, { name: 'Baidu' }],
      webTreeList: [
        {
          label: 'Google',
          children: [
            {
              label: 'Google-1.pcap',
            },
            {
              label: 'Google-2.pcap',
            },
            {
              label: 'Google-3.pcap',
            },
            {
              label: 'Google-4.pcap',
            }
          ],
        },
        {
          label: 'Github',
          children: [
            {
              label: 'github-1.pcap',
            },
            {
              label: 'github-2.pcap',
            },
            {
              label: 'github-3.pcap',
            },
            {
              label: 'github-4.pcap',
            }

          ],
        },
        {
          label: 'Wikipedia',
          children: [
            {
              label: 'Wikipedia-1.pcap',
            },
            {
              label: 'Wikipedia-2.pcap',
            },
            {
              label: 'Wikipedia-3.pcap',
            },
            {
              label: 'Wikipedia-4.pcap',
            }

          ],
        },
        {
          label: 'Faceboook',
          children: [
            {
              label: 'Faceboook-1.pcap',
            },
            {
              label: 'Faceboook-2.pcap',
            },

          ],
        },
      ],
      actionSequence: [{ label: 'Http1.1-get-request-html', color: '#E7EDF7', actionId: 0 },
      { label: 'Http2-get-request-image', color: '#D4E4F2', actionId: 1 },
      { label: 'Http2-get-request-image', color: '#BAD1E6', actionId: 2 },
      { label: 'Http2-get-request-image', color: '#F7E9E4', actionId: 3 },
      { label: 'Http2-get-request-image', color: '#E8D0D0', actionId: 4 }],
      //   trafficTableData:[{"color":"#E7EDF7",'Protocol':'HTTP/2','Type':'HEADERS (1)','RequestMethod':'GET',"AcceptType":'*/*',"RequestPacketNumber":87,"StatusCode":200,"ReasonPhrase":"OK","ContentType":'binary/octet-stream'},
      //   {"color":"#E7EDF7",'Protocol':'HTTP/2','Type':'HEADERS (1)','RequestMethod':'GET',"AcceptType":'*/*',"RequestPacketNumber":87,"StatusCode":200,"ReasonPhrase":"OK","ContentType":'binary/octet-stream'},
      //   {"color":"#D4E4F2",'Protocol':'HTTP/2','Type':'HEADERS (1)','RequestMethod':'GET',"AcceptType":'*/*',"RequestPacketNumber":87,"StatusCode":200,"ReasonPhrase":"OK","ContentType":'binary/octet-stream'},
      //   {"color":"#D4E4F2",'Protocol':'HTTP/2','Type':'HEADERS (1)','RequestMethod':'GET',"AcceptType":'*/*',"RequestPacketNumber":87,"StatusCode":200,"ReasonPhrase":"OK","ContentType":'binary/octet-stream'},
      //   {"color":"#BAD1E6",'Protocol':'HTTP/2','Type':'HEADERS (1)','RequestMethod':'GET',"AcceptType":'*/*',"RequestPacketNumber":87,"StatusCode":200,"ReasonPhrase":"OK","ContentType":'binary/octet-stream'},
      //   {"color":"#BAD1E6",'Protocol':'HTTP/2','Type':'HEADERS (1)','RequestMethod':'GET',"AcceptType":'*/*',"RequestPacketNumber":87,"StatusCode":200,"ReasonPhrase":"OK","ContentType":'binary/octet-stream'},
      //   {"color":"#F7E9E4",'Protocol':'HTTP/2','Type':'HEADERS (1)','RequestMethod':'GET',"AcceptType":'*/*',"RequestPacketNumber":87,"StatusCode":200,"ReasonPhrase":"OK","ContentType":'binary/octet-stream'},
      //   {"color":"#F7E9E4",'Protocol':'HTTP/2','Type':'HEADERS (1)','RequestMethod':'GET',"AcceptType":'*/*',"RequestPacketNumber":87,"StatusCode":200,"ReasonPhrase":"OK","ContentType":'binary/octet-stream'},
      //   {"color":"#E8D0D0",'Protocol':'HTTP/2','Type':'HEADERS (1)','RequestMethod':'GET',"AcceptType":'*/*',"RequestPacketNumber":87,"StatusCode":200,"ReasonPhrase":"OK","ContentType":'binary/octet-stream'},
      //   {"color":"#E8D0D0",'Protocol':'HTTP/2','Type':'HEADERS (1)','RequestMethod':'GET',"AcceptType":'*/*',"RequestPacketNumber":87,"StatusCode":200,"ReasonPhrase":"OK","ContentType":'binary/octet-stream'},
      //   {"color":"#E8D0D0",'Protocol':'HTTP/2','Type':'HEADERS (1)','RequestMethod':'GET',"AcceptType":'*/*',"RequestPacketNumber":87,"StatusCode":200,"ReasonPhrase":"OK","ContentType":'binary/octet-stream'}, ]
      // }
      trafficTableData: [
        { actionNo: 0, "color": "#E7EDF7", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 0, "color": "#E7EDF7", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": '443 -> 37022  [ACK] Seq=399 Ack=727 Win=373 Len=0 TSVal=3700939020 TSecr=82844624' },
        { actionNo: 1, "color": "#D4E4F2", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 1, "color": "#D4E4F2", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": '443 -> 37022  [ACK] Seq=399 Ack=727 Win=373 Len=0 TSVal=3700939020 TSecr=82844624' },
        { actionNo: 2, "color": "#BAD1E6", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 2, "color": "#BAD1E6", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": '443 -> 37022  [ACK] Seq=399 Ack=727 Win=373 Len=0 TSVal=3700939020 TSecr=82844624' },
        { actionNo: 3, "color": "#F7E9E4", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 3, "color": "#F7E9E4", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 0, "color": "#E7EDF7", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 0, "color": "#E7EDF7", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": '443 -> 37022  [ACK] Seq=399 Ack=727 Win=373 Len=0 TSVal=3700939020 TSecr=82844624' },
        { actionNo: 1, "color": "#D4E4F2", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 1, "color": "#D4E4F2", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 2, "color": "#BAD1E6", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 2, "color": "#BAD1E6", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 3, "color": "#F7E9E4", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 3, "color": "#F7E9E4", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 0, "color": "#E7EDF7", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 0, "color": "#E7EDF7", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 1, "color": "#D4E4F2", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 1, "color": "#D4E4F2", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 2, "color": "#BAD1E6", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 2, "color": "#BAD1E6", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 3, "color": "#F7E9E4", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 3, "color": "#F7E9E4", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 0, "color": "#E7EDF7", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 0, "color": "#E7EDF7", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 1, "color": "#D4E4F2", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 1, "color": "#D4E4F2", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 2, "color": "#BAD1E6", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 2, "color": "#BAD1E6", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 3, "color": "#F7E9E4", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 3, "color": "#F7E9E4", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
      ]
    }
  },
  methods: {
    increment() {
      this.count++
    },
    handleNodeClick(item) {
      console.log(item)
      this.getNetworkTraffic(item)
      this.currentActionOne = 1

    },
    getTableColor(id) {
      return this.actionSequence[id]
    },
    getNetworkTraffic(item) {

      this.currentWebName = item.label
      this.trafficTableData = []
      setTimeout(() => {
        this.trafficTableData = [
          { actionNo: 0, "color": "#E7EDF7", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 0, "color": "#E7EDF7", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": '443 -> 37022  [ACK] Seq=399 Ack=727 Win=373 Len=0 TSVal=3700939020 TSecr=82844624' },
          { actionNo: 1, "color": "#D4E4F2", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 1, "color": "#D4E4F2", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": '443 -> 37022  [ACK] Seq=399 Ack=727 Win=373 Len=0 TSVal=3700939020 TSecr=82844624' },
          { actionNo: 2, "color": "#BAD1E6", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 2, "color": "#BAD1E6", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": '443 -> 37022  [ACK] Seq=399 Ack=727 Win=373 Len=0 TSVal=3700939020 TSecr=82844624' },
          { actionNo: 3, "color": "#F7E9E4", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 3, "color": "#F7E9E4", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 0, "color": "#E7EDF7", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 0, "color": "#E7EDF7", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": '443 -> 37022  [ACK] Seq=399 Ack=727 Win=373 Len=0 TSVal=3700939020 TSecr=82844624' },
          { actionNo: 1, "color": "#D4E4F2", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 1, "color": "#D4E4F2", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 2, "color": "#BAD1E6", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 2, "color": "#BAD1E6", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 3, "color": "#F7E9E4", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 3, "color": "#F7E9E4", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 0, "color": "#E7EDF7", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 0, "color": "#E7EDF7", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 1, "color": "#D4E4F2", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 1, "color": "#D4E4F2", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 2, "color": "#BAD1E6", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 2, "color": "#BAD1E6", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 3, "color": "#F7E9E4", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 3, "color": "#F7E9E4", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 0, "color": "#E7EDF7", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 0, "color": "#E7EDF7", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 1, "color": "#D4E4F2", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 1, "color": "#D4E4F2", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 2, "color": "#BAD1E6", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 2, "color": "#BAD1E6", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 3, "color": "#F7E9E4", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 3, "color": "#F7E9E4", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
          { actionNo: 4, "color": "#E8D0D0", PacketNo: 1, 'Time': '6.204622', 'Protocol': 'TLSV1.2', 'Length': 166, "Info": 'Application Data' },
        ]

      }, 100)
    }
  },

  mounted() {
    // console.log(`.#FBB9A8`)

  }
}
</script>
<!-- <template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!1ssss1" />

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template> -->

<style scoped>
body{
  background: #fff!important;
}
.el-header {
  background-color: rgb(5 66 119);
  color: white;
  height: 50px;
  line-height: 50px;
  font-size: 20px;
  font-weight: 800;
}

.main {
  padding: 20px;
  background: #fff;
}

.container {
  display: flex;

}

.segmentation-panel {
  flex: 1;
}

.right-panel {
  width: 390px;
  margin-left: 20px;
}

.action-panel {
  margin-top: 20px;
  height: 150px;
}

.action-panel-label {
  width: 14px;
  height: 14px;
  display: inline-block;
  margin-left: 20px;
  margin-right: 10px;
  border-radius: 50%;
}

.action-panel-content {
  cursor: pointer;
  display: inline-block;
  line-height: 20px;
}

.action-panel-content:hover {
  color: rgb(92, 197, 242);
}

.action-list {
  display: flex;
  margin-top: 20px;
}

.highlightedText {
  color: white;
  font-weight: 600;
}


.web-list-item {
  cursor: pointer;
  line-height: 40px;
}

.web-list-item:hover {
  color: rgb(92, 197, 242);
}

.highlighted {
  color: rgb(92, 197, 242);
  font-weight: 800;
}

.action-panel-content.highlighted {
  color: rgb(254 128 95);
}

/deep/.el-table .cell {
  padding: 0;
}

.color-cell {
  /* height: 46px; */
  vertical-align: middle;
}

/deep/.el-table .el-table__cell {
  padding: 0;
}

.center-content {
  display: flex;
  justify-content: center;
  align-items: center;
}

.info-cell {
  font-family: monospace;
  /* font-weight: 800; */
  /* color: black; */
}
</style>
