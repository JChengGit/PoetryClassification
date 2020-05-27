<template>
<div style="margin:-7px; background-color:#fff4e8; height: 1200px">

<el-row>
  <el-col :span="7">
    <div style="height:44px;background-color:#545c64;color:#fff;text-align:left;font-family:STKaiti;padding-top:16px;
    font-size:22px; padding-left:120px;">古典诗词分析推荐系统</div>
  </el-col>
  <el-col :span="17">
    <el-menu style="height:59px"
      default-active="/classifier"
      router="true"
      class="el-menu-demo"
      mode="horizontal"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item index="/classifier" style="font-family:黑体;font-size:20px;">分析</el-menu-item>
      <el-menu-item index="/retrieve" style="font-family:黑体;font-size:20px;">查询</el-menu-item>
    </el-menu>
  </el-col>
</el-row>

<el-row style="margin-top:60px">
  <el-col :span="12" style="padding-left:120px;">
    <div><p  style="margin-top:0px; font-size: 18px;">请输入诗句:</p></div>
    <el-input
      type="textarea"
      :rows="6"
      placeholder="请输入内容"
      v-model="poet">
    </el-input>
    <el-button type="primary" style="margin-top:10px; margin-left:520px;"  @click="send">提交</el-button>
  </el-col>
  <el-col :span="12" style="padding-left:30px">
            <h3 style="margin-top:30px; margin-left:20px; font-size: 20px;">主题推断：</h3>
            <div style="height:20px"><p style="margin-left:20px; font-size:18px">{{topic}}</p></div>
            <h3 style="margin-top:30px; margin-left:20px; font-size: 20px;">情感推断：</h3>
            <div><p style="margin-left:20px; font-size:18px">{{emotion}}</p></div>
  </el-col>
</el-row>

<el-row>
  <p style="margin-top:20px; margin-left:120px; font-size: 22px;">诗词推荐</p>
</el-row>

<el-row>
  <el-col :span=16>
  <div v-for="item in rec" :key="item">
    <p style="margin-top:0px; margin-left:120px; font-size: 22px;font-family:STKaiti">{{item.title}}</p>
    <p style="margin-top:-15px; margin-left:120px; font-size: 15px;">{{item.author}}</p>
    <p style="margin-top:-15px; margin-left:120px; font-size: 18px;">{{item.content}}</p>
  </div>
  </el-col>
</el-row>

</div>
</template>

<script>
  export default {
    data() {
      return {

        topic: '',
        emotion: '',
        rec: '',
        poet:'',
        
      }
    },
    
    methods: {
      send: function() {
        this.axios.post('/api/classify/',{poet:this.poet}).then((res) => {
          this.topic = res.data.analysis[0];
          this.emotion = res.data.analysis[1];
          this.rec = res.data.recommend;
          console.log(this.rec);
        })
      }
    },
  }
</script>