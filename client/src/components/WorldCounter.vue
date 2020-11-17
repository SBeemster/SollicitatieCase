<template>
    <div class="world-counter">
        <h1>{{ count | longNumber }}</h1>
    </div>
</template>

<script>

const host = "127.0.0.1";
const port = 5678;

const intl = new Intl.NumberFormat();
const socket = new WebSocket(`ws://${host}:${port}`);

export default {
    name: "WorldCounter",
    data: function () {
        return {
            count: 0,
        };
    },
    mounted: function () {
        socket.onmessage = (event) => {
            this.count = Number.parseInt(event.data);
        };
    },
    filters: {
        longNumber: function (number) {
            return intl.format(number);
        },
    },
};

</script>

<style scoped lang="scss">
h1 {
    text-align: center;
}
</style>
