<template>
    <div id="app">
        <div class="panel">
            <div class="panel-head">
                <p class="panel-title">Current World Population</p>
            </div>
            <div class="panel-body">
                <WorldCounter />
            </div>
        </div>
        <div class="panel">
            <div class="panel-head">
                <p class="panel-title">World population</p>
            </div>
            <div class="panel-body">
                <p>
                    In demographics, the world population is the total number of
                    humans currently living, and was estimated to have reached
                    7,800,000,000 people as of March 2020. It took over 2
                    million years of human prehistory and history for the
                    world's population to reach 1 billion, and only 200 years
                    more to reach 7 billion.
                </p>
                <p>
                    The world population has experienced continuous growth
                    following the Great Famine of 1315–1317 and the end of the
                    Black Death in 1350, when it was near 370 million. The
                    highest global population growth rates, with increases of
                    over 1.8% per year, occurred between 1955 and 1975 – peaking
                    to 2.1% between 1965 and 1970. The growth rate declined to
                    1.2% between 2010 and 2015 and is projected to decline
                    further in the course of the 21st century. However, the
                    global population is still increasing and is projected to
                    reach about 10 billion in 2050 and more than 11 billion in
                    2100.
                </p>
                <p>
                    Source: <a
                        href="https://en.wikipedia.org/wiki/World_population"
                        target="_blank">Wikipedia</a>.
                </p>
            </div>
        </div>
    </div>
</template>

<script>
import WorldCounter from "./components/WorldCounter.vue";

export default {
    name: "App",
    components: {
        WorldCounter,
    },
};
</script>

<style lang="scss">
@import "@/assets/mustard-ui/panels.scss";

#app {
    font-family: Roboto, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    max-width: 1280px;
    margin-top: 60px;
    margin-left: auto;
    margin-right: auto;

    display: grid;
    align-items: center;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    column-gap: 20px;
    row-gap: 20px;

    .panel {
        height: 100%;
    }
}
</style>
