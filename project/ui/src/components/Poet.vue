<template>
  <div style="margin:-5px; padding-top:120px; background-color:#fff4e8;
              background-image:url('static/12.jpg');
              background-size: contain;
              background-repeat:no-repeat;">

  <div>
<ul>
    <li style="margin-left:230px; font-size:30px;" id="title"><a href="/#/">古典诗词分析推荐系统</a></li>
    <li style="font-size:26px "><a  href="/Poet">分析</a></li>
    <li style="font-size:26px"><a  class="active"  href="/Query">查询</a></li>
</ul>
  </div>
  
  <div style="margin-left:200px;">
    <div style="display:flex;">
        <div style="height:310px; width:800px;">
            <p  style="margin-top:0px; margin-left:55px; font-size: 22px;">请输入诗句:</p>
            <textarea style="margin-top:-10px; margin-left:50px; height:180px; width:700px; font-size:26px;"></textarea>
            
            <button style="width:242px;margin:2px; margin-left:512px; margin-top:10px; 
            background-color:#049eff;border:none;
            border-radius:4px; color:white;font-size:22px;padding-top:7px;padding-bottom:7px;" type="submit">提交</button>
        </div>
        <div style="height:320px; width:600px;">
            <h3 style="margin-top:30px; margin-left:20px; font-size: 27px;">主题推断：</h3>
            <p style="margin-left:20px; font-size:24px">山水景致</p>
            <h3 style="margin-top:30px; margin-left:20px; font-size: 27px;">情感推断：</h3>
            <p style="margin-left:20px; font-size:24px">喜悦</p>
        </div>
    </div>

    <div style="height:800px; width:1150px; padding:0px 30px;">
        <p style="margin-top:20px; margin-left:30px; font-size: 30px;">诗词推荐</p>
        
        <p style="margin-top:0px; margin-left:50px; font-size: 28px;font-family:STKaiti">《漁歌子》</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 20px;">唐 · 張志和</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 22px;">
          西塞山前白鷺飛，桃花流水鱖魚肥。青箬笠，綠蓑衣，斜風細雨不須歸。</p>
        
        <p style="margin-top:20px; margin-left:50px; font-size: 28px;font-family:STKaiti">《二月二日出郊》</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 20px;">宋 · 王庭珪</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 22px;">
          日頭欲出未出時，霧失江城雨腳微。
          天忽作晴山卷幔，雲猶含態石披衣。<br/>
          煙村南北黃鸝語，麥壟高低紫燕飛。
          誰似田家知此樂，呼兒吹笛跨牛歸？</p>
        
        <p style="margin-top:20px; margin-left:50px; font-size: 28px;font-family:STKaiti">《稻田》</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 20px;">唐 · 韋莊</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 22px;">
          綠波春浪滿前陂，極目連雲䎬稏肥。
          更被鷺鶿千點雪，破煙來入畫屏飛。</p>
        
        <p style="margin-top:20px; margin-left:50px; font-size: 28px;font-family:STKaiti">《巴女謠》</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 20px;">唐 · 于鵠</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 22px;">
          巴女騎牛唱竹枝，藕絲菱葉傍江時。
          不愁日暮還家錯，記得芭蕉出槿籬。</p>
        
        <p style="margin-top:20px; margin-left:50px; font-size: 28px;font-family:STKaiti">《春晚書山家·其二》</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 20px;">唐 · 貫休</p>
        <p style="margin-top:-15px; margin-left:55px; font-size: 22px;">
          水香塘黑蒲森森，鴛鴦鸂鶒如家禽。
          前村後壟桑柘深，東鄰西舍無相侵。<br/>
          蠶娘洗繭前溪淥，牧童吹笛和衣浴。
          山翁留我宿又宿，笑指西坡瓜豆熟。</p>
    </div>
    
  </div>  
  </div>
</template>

<script>
export default {

}
</script>

<style>

ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333;
    position: fixed;
    top: 0;
    width: 100%;
}

li {
    float: left;
}

li a {
    display: block;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
}

li a:hover:not(.active) {
    background-color: #111;
}

.active {
    background-color: #4CAF50;
}

#title {
   font-family:STKaiti;
}

</style>