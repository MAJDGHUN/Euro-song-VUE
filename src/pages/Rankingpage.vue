<template>

  <div>
     <button @click="goToPage('game')">
            Show game
        </button>

        <button @click="goToPage('ranking')">
            Show ranking
        </button>
        
        <button @click="goToPage('GoogleChart')">
            Show chart
        </button>
    <h1>Ranking</h1>
    
    <table>
      

      <tr>
        <th>Songs Ranking</th>

        <th>Song Title</th>

        <th>Song Artist</th>

        <th>Total Points</th>
       
        <th>Spotify</th>
      </tr>
      <tr v-for="(my_song, i) in All_Songs" :key="i">
        <td>--{{ ++i  }}--</td>
        <td>{{ my_song.title }}</td>
        <td>{{ my_song.artist }}</td>
        <td>{{ my_song.allPoints }}</td>
       
        <td>
         <iframe :src="my_song.spotify" width="100%" height="75" style="position:left;" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
        </td>
      </tr>
    </table>

  </div>

</template>

<script>
export default {
  name: "Rankingpage",

  data() {
    return {
      All_Songs: [],
      list:[],
    };
  },

  mounted() {
    this.fetchAll_Songs();
    this.fetchAll_Votes();
    this.fetchAll_Atists();
  },

  methods: {
    goToPage(page) {
      this.$emit("change-page", page);
    },

    
    fetchAll_Songs() {
    
      const url = "http://webservies.be/eurosong/Songs";
      fetch(url)
        .then((response) => {
          return response.json();
        })
        .then((All_Songs) => {

          this.fetchAll_Votes(All_Songs);
          this.fetchAll_Atists(All_Songs);
        });
    },

    fetchAll_Atists(All_Songs) {
      const url = "http://webservies.be/eurosong/Artist";
      fetch(url)
        .then((response) => {
          return response.json();
        })
        .then((All_Atists) => {
          All_Songs.map((my_song) => {
            const a = All_Atists.find((artist) => artist.id == my_song.artist);
            my_song.artist = a.name;
            
            return my_song;
          });
          this.All_Songs = All_Songs;
        });
    },

    fetchAll_Votes(All_Songs) {
      const url = "http://webservies.be/eurosong/Votes";
      fetch(url)
        .then((response) => {

          return response.json();
        })
        .then((All_Votes) => {
          
          All_Songs.map((my_song) => {
            my_song.allPoints = 0;
            All_Votes
              .filter((vote) => vote.songID == my_song.id)
              .forEach((element) => {
                if (element.songID == my_song.id) {
                  my_song.allPoints = (my_song.allPoints+element.points);
                
                }
              });
            return my_song;
          });
          this.All_Songs = All_Songs.sort((a, b) => b.allPoints - a.allPoints);
        });
    },
  },
};
</script>