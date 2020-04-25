<template>
  <div style="margin:-5px; padding-top:120px; background-color:#fff4e8;
              background-image:url('static/12.jpg');
              background-size: contain;
              background-repeat:no-repeat;">


  
  <div style="margin-left:200px;">
    <p style="margin-top:10px; margin-left:80px; font-size: 20px;">请选择：</p>
    <div style="display:flex;">

      <el-select v-model="value1" placeholder="请选择主题" style="margin-left:80px" size="medium">
        <el-option
          v-for="item in topic"
          :key="item.value"
          :label="item.label"
          :value="item.value">
        </el-option>
      </el-select>
      
      <el-select multiple v-model="value2" placeholder="请选择情感" style="margin-left:30px;" size="medium">
        <el-option
          v-for="item in emotion"
          :key="item.value"
          :label="item.label"
          :value="item.value"
          style="">
        </el-option>
      </el-select>

      <button style="width:120px;margin:2px; margin-left:30px; margin-top:0px; 
            background-color:#049eff;border:none;
            border-radius:4px; color:white;font-size:14px;padding-top:7px;padding-bottom:7px;" type="submit">查询
      </button>
    </div>

    <div style="height:2800px; width:1150px; padding:0px 30px;">
        <p style="margin-top:40px;" ></p>
        
        <p style="margin-top:0px; margin-left:50px; font-size: 24px;font-family:STKaiti">《虢州後亭送李判官使赴》</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 16px;">唐 · 岑參</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 16px;">
          西原驛路掛城頭，客散紅亭雨未收。君去試看汾水上，白雲猶似漢時秋。</p>
        
        <p style="margin-top:20px; margin-left:50px; font-size: 24px;font-family:STKaiti">《古別離》</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 16px;">唐 · 孟郊</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 16px;">
          欲別牽郎衣，郞今到何處？不恨歸來遲，莫向臨邛去。
        
        <p style="margin-top:20px; margin-left:50px; font-size: 24px;font-family:STKaiti">《點絳唇·途中逢管倅》</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 16px;">宋 · 趙彥端</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 16px;">
          憔悴天涯，故人相遇情如故。別離何遽，忍唱陽關句。<br/>
          我是行人，更送行人去。愁無據。寒蟬鳴處，回首斜陽暮。</p>
        
        <p style="margin-top:20px; margin-left:50px; font-size: 24px;font-family:STKaiti">《普天樂·秋江憶別》</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 16px;">元 · 趙善慶</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 16px;">
          晚天長，秋水蒼。山腰落日，雁背斜陽。壁月詞，朱唇唱。<br/>
          猶記當年蘭舟上，灑西風淚濕羅裳。釵分鳳凰，杯斟鸚鵡，人拆鴛鴦。</p>
        
        <p style="margin-top:20px; margin-left:50px; font-size: 24px;font-family:STKaiti">《臨江仙》</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 16px;">宋 · 晏幾道</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 16px;">
          淡水三年歡意，危弦幾夜離情。曉霜紅葉舞歸程。客情今古道，秋夢短長亭。<br/>
          淥酒尊前清淚，陽關疊裏離聲。少陵詩思舊才名。雲鴻相約處，煙霧九重城。</p>

        <p style="margin-top:20px; margin-left:50px; font-size: 24px;font-family:STKaiti">《別雲間》</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 16px;">明 · 夏完淳</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 16px;">
          三年羈旅客，今日又南冠。無限山河淚，誰言天地寬。<br/>
          已知泉路近，欲別故鄉難。毅魄歸來日，靈旗空際看。</p>
        
        <p style="margin-top:20px; margin-left:50px; font-size: 24px;font-family:STKaiti">《送路六侍禦入朝》</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 16px;">唐 · 杜甫</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 16px;">
          童稚情親四十年，中間消息兩茫然。更為後會知何地？忽漫相逢是別筵！<br/>
          不分桃花紅似錦，生憎柳絮白於棉。劍南春色還無賴，觸忤愁人到酒邊。</p>
        
        <p style="margin-top:20px; margin-left:50px; font-size: 24px;font-family:STKaiti">《重別李評事》</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 16px;">唐 · 王昌齡</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 16px;">
          莫道秋江離別難，舟船明日是長安。吳姬緩舞留君醉，隨意青楓白露寒。</p>
    </div>
    
  </div>  
  </div>
</template>

<script>
export default {
    data() {
      return {
        topic: [{
          value: '选项1',
          label: '咏史怀古'
        }, {
          value: '选项2',
          label: '离别送别'
        }, {
          value: '选项3',
          label: '战争边塞'
        }, {
          value: '选项4',
          label: '山水景致'
        }, {
          value: '选项5',
          label: '行旅思乡'
        }, {
          value: '选项6',
          label: '爱情闺怨'
        }],

        emotion: [{
          value: '选项1',
          label: '悲伤'
        }, {
          value: '选项2',
          label: '喜悦'
        }, {
          value: '选项3',
          label: '忧愁'
        }, {
          value: '选项4',
          label: '豪迈'
        }, {
          value: '选项5',
          label: '愤怒'
        }],

        value1: '',
        value2: '',
      }
    }
}
</script>

<style>


</style>