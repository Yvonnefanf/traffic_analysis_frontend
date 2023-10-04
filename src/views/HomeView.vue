<script setup>
import { RouterLink, RouterView } from 'vue-router'


</script>
<template>
  <div v-loading="isLoading" loading-text="analysising...">
    <el-upload :action="'/api/upload'" :on-success="handleSuccess" :before-upload="beforeUpload">
      <el-button slot="trigger" type="primary">select PCAP file</el-button>
      <template #tip>
        <div class="el-upload__tip">
          only accept .pcap files
        </div>
      </template>
    </el-upload>
    <el-card>
      <el-table :data="tableData" height="calc(100vh - 300px)" width="100%">
        <el-table-column label="Time" width="220">
          <template #default="scope">
            <div class="color-cell">
              {{ scope.row.Time }}
            </div>
          </template>
        </el-table-column>
        <el-table-column label="Length" width="120">
          <template #default="scope">
            <div class="color-cell">
              {{ scope.row.length }}
            </div>
          </template>
        </el-table-column>
        <el-table-column label="Protocol" width="120">
          <template #default="scope">
            <div class="color-cell">
              {{ scope.row.protocol }}
            </div>
          </template>
        </el-table-column>
        <el-table-column label="info">
          <template #default="scope">
            <div class="color-cell">
              {{ scope.row.info || '--' }}
            </div>
          </template>
        </el-table-column>
      </el-table>
      <div style="height: 70px;">
        <el-button @click="startAnalysis" type="primary" style="margin-left: 92%; margin-top: 20px;">Analysis</el-button>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {

  data() {
    return {
      tableData: [],
      pcapPath: '',
      isLoading: false
    }
  },
  methods: {
    handleSuccess(response, file) {
      console.log('File uploaded successfully:', file);
      console.log("response", response)
      this.tableData = response.data
      this.pcapPath = response.path
    },
    beforeUpload(file) {
      const isPCAP = file.name.endsWith('.pcap');
      if (!isPCAP) {
        this.$message.error('upload file need .pcap 格式!');
      }
      return isPCAP;
    },
    startAnalysis() {
      const params = {
        pcapPath: this.pcapPath,
      };
      console.log(params); // 确保 params 包含正确的数据
      this.isLoading = true
      setTimeout(()=>{
        this.isLoading = false
        this.$router.push({ name: 'about', query: { pcapPath: this.pcapPath }  });
      }, 1000)
      
      
    }
  },

  mounted() {

    // console.log(`.#FBB9A8`)

  }
}
</script>
<!-- <template>
  <header>
   
    <div class="wrapper">
      <HelloWorld msg="You did it!1ssss1" />

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>


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
  background: #fff;
  height: calc(100vh);
}

.container {
  width: 100%;
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



.color-cell {
  height: 46px;
  line-height: 46px;
  vertical-align: middle;
  /* font-family: monospace; */
}

/* /deep/.el-table .el-table__cell {
  padding: 0;
}
/deep/.el-table .cell {
  padding: 0;
} */

.center-content {
  display: flex;
  justify-content: center;
  align-items: center;
}

.info-cell {
  font-family: monospace;
  /* font-weight: 800; */
  /* color: black; */
  text-align: left;
  white-space: nowrap;
}



</style>
