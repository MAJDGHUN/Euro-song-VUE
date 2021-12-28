<template>
    <div v-if="isVisible">
        Buttoncounter: {{ count }}

        <button @click="addOne">
            Add 1
        </button>

        <button @click="minOne">
            Min 1
        </button>

        <button @click="hide">
            hide
        </button>
    </div>
</template>

<script>
    export default {
        name: "Counter",
        data() {
            return {
                count: 10,
                isVisible: true,
                homeUrl: "contact.html"
            }
        },
        methods: {
            addOne() {
                this.count++;
            },
            minOne() {
                this.count--;
            },
            hide() {
                this.isVisible = false;
            }
        }
    }
</script>