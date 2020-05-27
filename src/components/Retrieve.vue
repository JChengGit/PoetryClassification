<template>
<div style="margin:-7px; background-color:#fff4e8; height: 1200px">

  <el-row>
    <el-col :span="7">
      <div style="height:44px;background-color:#545c64;color:#fff;text-align:left;font-family:STKaiti;padding-top:16px;
      font-size:22px; padding-left:120px;">古典诗词分析推荐系统</div>
    </el-col>
    <el-col :span="17">
      <el-menu style="height:59px"
        default-active="/retrieve"
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

  <div style="margin-top:40px; display:flex;">

    <el-select v-model="topic" placeholder="请选择主题" style="margin-left:120px" size="medium">
      <el-option
        v-for="item in topic_list"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
    </el-select>
    
    <el-select v-model="emotion" placeholder="请选择情感" style="margin-left:30px;" size="medium">
      <el-option
        v-for="item in emotion_list"
        :key="item.value"
        :label="item.label"
        :value="item.value">
      </el-option>
    </el-select>

    <el-button style="margin-left:50px" @click="send" type="primary" size="medium">查询</el-button>
  </div>

  <el-row style="margin-top:30px">
    <el-col :span=16>
    <div v-for="item in list" :key="item">
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
        topic_list: [{
          value: 'history',
          label: '咏史怀古'
        }, {
          value: 'farewell',
          label: '离别送别'
        }, {
          value: 'war',
          label: '战争边塞'
        }, {
          value: 'scene',
          label: '山水景致'
        }, {
          value: 'travel',
          label: '行旅思乡'
        }, {
          value: 'love',
          label: '爱情闺怨'
        }],

        emotion_list: [{
          value: 'sad',
          label: '悲伤'
        }, {
          value: 'happy',
          label: '喜悦'
        }, {
          value: 'sorrow',
          label: '忧愁'
        }, {
          value: 'heroic',
          label: '豪迈'
        }, {
          value: 'angry',
          label: '愤怒'
        }],

        topic: '',
        emotion: '',
        page:1,
        list: '',

      }
    },
    
    methods: {
      send: function() {
        this.axios.get('/api/retrieve/',{params:{
          topic:this.topic,
          emotion:this.emotion,
          page:this.page,
        }}).then((res) => {
          this.list = res.data;
          console.log(res.data);
        })
      }
    },
}
</script>

<style>


</style>