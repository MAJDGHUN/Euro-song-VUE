<template>
    <div>
        <button id="11" @click="changeIndex(-1)">
            Prev song
        </button>
        <div v-for="(song, index) in items" :key="song.id">
            <div v-if="index == activeIndex">
                {{ song.artist.name}} - {{ song.title }}
                <p></p>
                <iframe :src="song.spotify" width="23%" height="80" style="position:left;" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>
            </div>
        </div>
        <button id="12" @click="changeIndex(1)">
            Next song
        </button>
    </div>
</template>

<script>
    export default {
        name: "Carousel",
        props: [
            "items",
            "activeIndex"
        ],
        methods: {
            changeIndex(value) {
                // copy, you can not change props directly
                let index = this.activeIndex;

                // -1 of 1;
                index += value;

                // check if index is the beginning or ending
                if (index < 0) {
                    index = this.items.length -1;
                } else if (index == this.items.length) {
                    index = 0;
                }

                // change index in gamepage
                this.$emit("change-index", index);
            }
        }
    }
</script>