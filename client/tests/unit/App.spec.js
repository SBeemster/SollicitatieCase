import { mount } from "@vue/test-utils";
import App from "@/App.vue";
import WorldCounter from "@/components/WorldCounter.vue";


describe("App.vue", () => {
    it("loads WorldCounter", () => {
        const wrapper = mount(App);
        const worldCounter = wrapper.findComponent(WorldCounter);

        expect(worldCounter.exists()).toBe(true);
    })
})