<template>
  <div>
    <h2>Vue Js Google Column or Bar Chart Demo</h2>
    <button @click="goToPage('game')">Show game</button>

    <button @click="goToPage('ranking')">Show ranking</button>

    <button @click="goToPage('GoogleChart')">Show chart</button>

    <GChart type="ColumnChart" :options="options" :data="data" />
    <GChart type="PieChart" :options="options" :data="data" />
  </div>
</template>
 
<script>
import { GChart } from "vue-google-charts";
import Rankingpage from "../pages/Rankingpage.vue";

export default {
  name: "App",

  components: {
    GChart,
    Rankingpage,
  },
  props: {
    label: {
      type: Array,
    },
    chartData: {
      type: Array,
    },
  },

  data() {
    return {
      songs: [],
      //Ik heb geprobeerd om de data te halen van ranking-vue als array maar het lukte niet-> dit zeker geen real-time data
      data: [
        ["Song Title", "Total Points", { role: "style" }],
        ["Sweden	", 1921, "#6B58E2"],
        ["Shinzou Wo Sasageyo	", 970, "#00B28F"],
        ["Technicolor	", 615, "#F8D12F"],
        ["Mata Hari", 516, "color: #e5e4e2"],
        ["Amen", 499, "color: #4E6973"],
        ["The Wrong Place	", 490, "color: #4E6973"],
        ["Mad about you", 453, "color: #4E6973"],
        ["King Of The Fall", 360, "color: #4E6973"],
        ["Sex Offender Shuffle", 188, "color: #4E6973"],
        ["Bye Bye", 74, "color: #4E6973"],
        ["Man's Not Hot", 53, "color: #4E6973"],
        ["The Muffin Song", 46, "color: #4E6973"],
        ["Gay Trump Porn", 38, "color: #4E6973"],
        ["	precipice of defeat Believe in YourSelf & theres no defeat", 20, "color: #4E6973"],
      ],
      options: {
        width: 1100,
        height: 400,
      },
    };
  },

  mounted() {
    
    this.renderChart(this.songs);
  },

  methods: {
    goToPage(page) {
      this.$emit("change-page", page);
    },

    
  },
};
</script>
