import { shallowMount } from "@vue/test-utils";
import WorldCounter from "@/components/WorldCounter.vue";

describe("WorldCounter.vue", () => {
    it("displays the value 3", () => {
        const value = 3;
        const wrapper = shallowMount(WorldCounter, {
            data: function() {
                return {
                    count: value
                }
            }
        });
        expect(wrapper.text()).toMatch(value.toString());
    }),
    it("displays a random value < 1000", () => {
        const value = (Math.random() * 1000) >>> 0;
        const wrapper = shallowMount(WorldCounter, {
            data: function() {
                return {
                    count: value
                }
            }
        });
        expect(wrapper.text()).toMatch(value.toString());
    }),
    it("displays the value 376565, formatted", () => {
        const value = 376565;
        const formatted = new Intl.NumberFormat().format(value);
        const wrapper = shallowMount(WorldCounter, {
            data: function() {
                return {
                    count: value
                }
            }
        });
        expect(wrapper.text()).toMatch(formatted);
    }),
    it("displays a random value > 1000, formatted", () => {
        const value = (1000 + (Math.random() * 100000000)) >>> 0;
        const formatted = new Intl.NumberFormat().format(value);
        const wrapper = shallowMount(WorldCounter, {
            data: function() {
                return {
                    count: value
                }
            }
        });
        expect(wrapper.text()).toMatch(formatted);
    })
})
