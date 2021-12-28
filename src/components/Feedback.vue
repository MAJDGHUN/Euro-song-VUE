<template>
    <div :class="'c-feedback ' + classType" v-if="isActive" @click="hide">
        {{ message }}
        {{ classType }}
    </div>
</template>

<script>
    export default {
        name: "Feedback",
        data() {
            return {
                isActive: true
            }
        },
        props: [
            'message',
            'classType'
        ],
        methods: {
            hide() {
                this.isActive = false;
            }
        }
    }
</script>
