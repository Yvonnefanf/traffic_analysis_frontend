<script setup>
import { RouterLink, RouterView } from 'vue-router'


</script>
<template>
  <div class="main">


    <div class="container">



      <el-card class="segmentation-panel" style="position: relative;">

        <!-- <el-divider /> -->
        <div style="display: flex;">
          <div style="flex: 1; width: 66%;">
            <h3 style="display: inline-block;">Network Traffic</h3> <span style="margin-left: 20px;"><el-tag>{{ pcapPath
            }}</el-tag></span>
            <!-- <el-button style="position: absolute; right: 120px;" @click="showColor">
          Predict
        </el-button> -->

            <!-- <el-button style="position: absolute; right: 30px;">
          <RouterLink to="/">Home</RouterLink>
        </el-button> -->
            <div style="margin-top: 8px;">
              <!-- <div
                style="height: 10px; width:10px; border-radius: 50%; background-color: rgb(255, 0, 153); display: inline-block; margin-right: 20px;">
              </div> Highlight Web -->
              <div
                style="height: 10px; width:10px; border-radius: 50%; background-color: rgb(254 128 95); display: inline-block;">
              </div> Highlight Action

              <el-switch v-model="ifFilter" class="ml-2" @change="getTrafficData" style="margin-left: 20px;" /> Filter
              Action
            </div>
            <el-table v-loading="isLoading" height="calc(100vh - 280px)" :data="currentData">

              <el-table-column label="Packet No." width="90">
                <template #default="scope">
                  <div class="color-cell center-content"
                    :class="{ highlightedText: (scope.row.actionId === currentActionId || (currentWeb != null && scope.row.Website == currentWeb?.url)) }"
                    :style="{ backgroundColor: (currentWeb != null && scope.row.Website == currentWeb?.url) ? 'rgb(255, 0, 153)' : (scope.row.actionId == currentActionId ? 'rgb(254 128 95)' : (withColor ? getColor(scope.row.Action) : 'white')) }">
                    {{ scope.row["Packet No."] || '-' }}
                    <!-- {{  currentWeb?.url }} -->
                  </div>
                </template>
              </el-table-column>
              <el-table-column label="Time" width="200">
                <template #default="scope">
                  <div class="color-cell" :class="{ highlightedText: scope.row.actionId === currentActionId }"
                    :style="{ backgroundColor: scope.row.actionId == currentActionId ? 'rgb(254 128 95)' : (withColor ? getColor(scope.row.Action) : 'white') }">
                    {{ scope.row.Time || '-' }}
                  </div>
                </template>
              </el-table-column>
              <el-table-column label="Protocol" width="70">
                <template #default="scope">
                  <div class="color-cell" :class="{ highlightedText: scope.row.actionId === currentActionId }"
                    :style="{ backgroundColor: scope.row.actionId == currentActionId ? 'rgb(254 128 95)' : (withColor ? getColor(scope.row.Action) : 'white') }">
                    {{ scope.row.Protocol || '-' }}
                  </div>
                </template>
              </el-table-column>
              <el-table-column label="Length" width="70">
                <template #default="scope">
                  <div class="color-cell" :class="{ highlightedText: scope.row.actionId === currentActionId }"
                    :style="{ backgroundColor: scope.row.actionId == currentActionId ? 'rgb(254 128 95)' : (withColor ? getColor(scope.row.Action) : 'white') }">
                    {{ scope.row.Length || '-' }}
                  </div>
                </template>
              </el-table-column>

              <!-- <el-table-column label="Action" width="180">
                <template #default="scope">

                  <div class="color-cell info-cell" :class="{ highlightedText: scope.row.Action === currentActionId }"
                    :style="{ backgroundColor: scope.row.Action == currentActionId ? 'rgb(254 128 95)' : (withColor ? getColor(scope.row.Action) : 'white') }">
                    {{ scope.row.Action || '--' }}
                  </div>
                </template>
              </el-table-column> -->
              <!-- <el-table-column label="Downstream Task" width="140">
                <template #default="scope">

                  <div class="color-cell info-cell" :class="{ highlightedText: scope.row.actionId === currentActionId }"
                    :style="{ backgroundColor: scope.row.actionId == currentActionId ? 'rgb(254 128 95)' : (withColor ? getColor(scope.row.Action) : 'white') }">
                    {{ scope.row['Downstream Task'] || '--' }}
                  </div>
                </template>
              </el-table-column> -->

              <el-table-column label="Info">
                <template #default="scope">

                  <div class="color-cell info-cell" :class="{ highlightedText: scope.row.actionId === currentActionId }"
                    :title="scope.row.Info"
                    :style="{ backgroundColor: scope.row.actionId == currentActionId ? 'rgb(254 128 95)' : (withColor ? getColor(scope.row.Action) : 'white') }">
                    {{ scope.row.Info || '-' }}
                  </div>
                </template>
              </el-table-column>




            </el-table>
            <el-pagination style="margin-top: 10px;" @size-change="handleSizeChange" @current-change="handleCurrentChange"
              :current-page="currentPage" :page-sizes="[500, 1000, 3000]" :page-size=pageSize
              layout="total, sizes, prev, pager, next, jumper" :total="totalDataCount">
            </el-pagination>
          </div>
          <el-divider direction="vertical" style="height: calc(100vh - 170px);" />
          <div style="{width: 24%;}">
            <div style="margin-left: 20px;">
              <h3>Action Sequence</h3>
              <div style="margin:20px 0;">
                <el-button style="width: 100px; white-space: normal;" @click="showWeb = true">Website
                  fingerprinting</el-button>
                <el-button style="width: 100px; white-space: normal;" :disabled="true">malware analysis</el-button>
                <el-button style="width: 100px; white-space: normal;" :disabled="true">intrusion detection</el-button>

              </div>
            </div>
            <div style="height: calc(100vh - 300px); width:100%; overflow: auto;">
              <div style="font-size: 13px;" v-for="item in actionSeq" @click="currentActionId = item.actionId">
                <div class="action-panel-label" :style="{ backgroundColor: item.color }"></div>
                <div class="action-panel-content" :class="{
                  highlighted: currentActionId === item.actionId,
                  highlightedPink: currentWeb?.action[0] <= item.actionId && currentWeb?.action[1] >= item.actionId
                }">{{ item.label }}
                </div>
              </div>
            </div>

          </div>

        </div>



      </el-card>
      <el-card class="right-panel">
        <!-- <el-button style="position: absolute; right: 60px;" @click="showColor">
          Predict
        </el-button> -->

        <el-tabs v-model="activeName" class="demo-tabs" style="margin-top: 50px;">
          <el-tab-pane label="Web" name="web">

            <ul v-if="showWeb">
              <li v-for="item in webList" :class="{ highlighted: currentWeb?.name === item.name }" class="web-list-item"
                @click="getNetworkTraffic(item)">
                <span style="font-weight: 800;">{{ item.name }}</span>
                <br /><a style="font-size: 12px; display: inline-block; margin-bottom: 6px;">{{ item.url }}</a>
              </li>


            </ul>

          </el-tab-pane>
          <el-tab-pane label="Intrusion" name="Intrusion" :disabled="true">2</el-tab-pane>
          <el-tab-pane label="Malware" name="malware" :disabled="true">3</el-tab-pane>
          <!-- <el-tab-pane label="Applic" name="applic" :disabled="true">4</el-tab-pane> -->
        </el-tabs>

      </el-card>



    </div>
    <!-- <div class="footer">
      <el-card class="action-panel">
        <h3>Action Sequence</h3>
        <div class="action-list">
          <div v-for="item in actionSequence" @click="currentActionId = item.label">
            <div class="action-panel-label" :style="{ backgroundColor: item.color }"></div>
            <div class="action-panel-content" :class="{ highlighted: currentActionId === item.label }">{{ item.label }}
            </div>
          </div>
        </div>

      </el-card>


    </div> -->
  </div>
</template>
<script>
import Api from "../libs/api";
export default {

  data() {
    return {
      ifFilter: true,
      withColor: true,
      showWeb: false,
      currentPage: 1,
      pageSize: 500,
      totalDataCount: 0,
      currentData: [],
      showTable: false,
      isLoading: false,
      activeName: 'web',
      currentWeb: null,
      pcapPath: '--',
      activeTableName: 'Traffic',
      actionSequenceColorDict: {
        0: "#E7EDF7",
        1: "#D4E4F2",
        2: "#BAD1E6",
        3: "#F7E9E4",
        4: "#E8D0D0"
      },
      currentActionId: '-',
      currentActionOne: null,
      currentActionList: [0, 0],
      webList: [
        { name: 'CHSI', url: 'www.chsi.com.cn', action: [0, 14] },
        { name: 'JD', url: 'union-click.jd.com', action: [15, 201] },
        { name: 'Sogou', url: 'www.sogou.com', action: [202, 217] },
        { name: 'Baidu', url: 'www.baidu.com', action: [218, 227] },
        { name: 'QQ', url: 'www.qq.com', action: [228, 333] },
        { name: 'Sina weibo', url: 'www.sina.com.cn', action: [334, 375] },
        { name: 'Ctrip', url: 'www.ctrip.com', action: [0, 0] },


        { name: '163 Mail', url: 'www.163.com', action: [] },
        { name: 'Jumpluna', url: 'jumpluna.58.com', action: [0, 0] },
        { name: 'Taobao', url: 'www.taobao.com', action: [0, 0] },


      ],

      // showAction:[{ label: 'Open website', color: '#E7EDF7', actionId: 0 },
      // { label: 'Browse website', color: '#BAD1E6', actionId: 1 },
      // { label: 'Click hyperlink a', color: '#F7E9E4', actionId: 2 },
      // { label: 'Click hyperlink b', color: '#E8D0D0', actionId: 3 }],


      actionSeq: [],
      actionSequence: [{ label: 'http/1.1-post-*/*', color: '#E7EDF7', actionId: 0 },
      { label: 'http/1.1-response-200-OK-application/ocsp-response', color: '#BAD1E6', actionId: 1 },
      { label: 'http/1.1-get-text/html', color: '#F7E9E4', actionId: 2 },
      { label: 'http/1.1-response-302-Found-*/*', color: '#E8D0D0', actionId: 3 },
      { label: 'http/1.1-response-200-OK-text/html', color: '#F0C9DC', actionId: 4 },
      { label: 'http/1.1-get-text/css', color: '#ECDED9', actionId: 5 },
      { label: 'http/1.1-get-*/*', color: '#C3DBC2', actionId: 6 },
      { label: 'http/1.1-response-200-OK-text/css', color: '#D4D392', actionId: 7 },
      { label: 'http/1.1-response-200-OK-application/javascript', color: '#C9C88F', actionId: 8 },
      { label: 'http/1.1-get-image/avif', color: '#B0C7D1', actionId: 9 },
      { label: 'http/1.1-response-200-OK-image/png', color: '#E4E8EB', actionId: 10 },
      { label: 'http/1.1-response-200-OK-*/*', color: '#A6F075', actionId: 11 },
      { label: 'http/1.1-post-application/json', color: '#8694CD', actionId: 12 },
      { label: 'http/1.1-get-application/json', color: '#B0C5FC', actionId: 13 },
      { label: 'http/1.1-response-200-OK-application/json', color: '#D6ABD8', actionId: 14 },
      { label: 'http/1.1-get-application/font-woff2', color: '#BCDDF3', actionId: 15 },
      { label: 'http/1.1-response-200-OK-font/woff2', color: '#E5DBB6', actionId: 16 },
      { label: 'http/1.1-response-200-OK-image/jpeg', color: '#E6B988', actionId: 17 },
      { label: 'http/1.1-response-200-OK-image/x-icon', color: '#B9D6CE', actionId: 18 },
      { label: 'http/1.1-response-302-Found-text/html', color: '#f4c7a8', actionId: 19 },
      { label: 'http/1.1-response-200-OK-image/webp', color: '#98A2C6', actionId: 20 },
      ],

      trafficTableData: [
      ]
    }
  },
  methods: {
    increment() {
      this.count++
    },
    getColor(str) {
      const action = this.actionSequence.find(action => action.label == str);
      return action ? action.color : 'white';

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

      this.currentWeb = item
      this.currentActionList = item.action
      // this.showAction = []
      console.log(this.currentWeb.action)
      // for(let i=0;i<this.currentWeb.action.length;i++){
      //   let index = this.currentWeb.action[i]
      //   this.showAction.push(this.actionSequence[index])
      // }


    },
    showColor() {
      this.showAction = [{ label: 'Open website', color: '#E7EDF7', actionId: 0 },
      { label: 'Browse website', color: '#BAD1E6', actionId: 1 },
      { label: 'Click hyperlink a', color: '#F7E9E4', actionId: 2 },
      { label: 'Click hyperlink b', color: '#E8D0D0', actionId: 3 }]
      this.withColor = true
      this.showWeb = true

    },
    getTrafficData() {
      let that = this
      this.isLoading = true

      Api.getTraffic({ ifFilter: this.ifFilter }).then((res) => {

        const data = typeof res.data === 'string' ? JSON.parse(res.data) : res.data;
        // console.log(data);
        // 过滤掉 action 为空的数据
        that.totalData = data.result;
        that.actionSeq = data.actions_array
        that.actionSeq.forEach(action => {
          action.color = this.getColor(action.label);
        });

        that.totalDataCount = that.totalData.length
        that.handleCurrentChange(1);
        that.isLoading = false



      })
    },
    handleSizeChange(val) {
      this.currentData = this.totalData.slice(0, val);
      this.pageSize = val;
    },
    handleCurrentChange(val) {
      this.currentPage = val;
      this.currentData = this.totalData.slice(
        (val - 1) * this.pageSize, // 50 是每页的数据量
        val * this.pageSize
      );
    },

  },

  mounted() {
    this.pcapPath = this.$route.query.pcapPath
    this.getTrafficData()


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
        <RouterLink to="/.">About</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template> -->

<style scoped>
.el-header {
  background-color: rgb(5 66 119);
  color: white;
  height: 70px;
  line-height: 70px;
  font-size: 20px;
  font-weight: 800;
}

.main {
  padding: 20px;
  width: 100%;
}

.container {
  display: flex;
  height: calc(100vh - 130px);

}

.segmentation-panel {
  flex: 1;
}

.right-panel {
  width: 300px;
  margin-left: 20px;
}

.action-panel {
  margin-top: 20px;
  height: 170px;
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
  margin-top: 10px;
  flex-wrap: wrap;
}

.highlightedText {
  color: white;
  font-weight: 600;
}


.web-list-item {
  cursor: pointer;
  line-height: 20px;
  margin-top: 10px;
}

.web-list-item:hover {
  /* color: rgb(92, 197, 242); */
  color: rgb(255, 0, 153, 0.6);
}

.highlighted {
  /* color: rgb(92, 197, 242); */
  color: rgb(255, 0, 153);
  /* font-weight: 800; */
}
.highlightedPink{
  color: rgb(255, 0, 153);
  /* font-weight: 800; */
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
  font-size: 12px;
}

.center-content {
  display: flex;
  justify-content: center;
  align-items: center;

}

.info-cell {
  font-family: monospace;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  font-size: 12px;
  /* font-weight: 800; */
  /* color: black; */
}
</style>
