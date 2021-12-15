<template>
  <form class="row g-3">
    <div class="col">
      <AnalyseInput
        inputName="Support"
        @change="onSupportChange"
        :value="support"
      />
      <AnalyseInput
        inputName="Confidence"
        @change="onConfidenceChange"
        :value="confidence"
      />
      <AnalyseInput inputName="Lift" @change="onLiftChange" :value="lift" />
    </div>

    <div class="mb-3 form-check">
      <input type="checkbox" class="form-check-input" id="exampleCheck1" />
      <label class="form-check-label" for="exampleCheck1">Check me out</label>
    </div>

    <button type="submit" class="btn btn-primary" @click.prevent="onSubmit">
      Submit
    </button>
  </form>
</template>

<script>
import store from "@/store/index.js";
import AnalyseInput from "./AnalyseInput.vue";
import { mapActions, mapMutations, mapState } from "vuex";
export default {
  name: "AnalyseForm",
  components: {
    AnalyseInput,
  },
  store,
  computed: {
    ...mapState({
      support: (state) => state.analyse.support,
      confidence: (state) => state.analyse.confidence,
      lift: (state) => state.analyse.lift,
    }),
  },
  methods: {
    ...mapMutations({
      setSupport: "analyse/setSupport",
      setConfidence: "analyse/setConfidence",
      setLift: "analyse/setLift",
    }),
    ...mapActions({
      getRules: "analyse/getRules",
    }),
    onSupportChange(e) {
      try {
        this.setSupport(parseFloat(e.target.value));
      } catch (error) {
        console.error(error);
        this.setSupport(0.01);
      }
    },
    onConfidenceChange(e) {
      try {
        this.setConfidence(parseFloat(e.target.value));
      } catch (error) {
        console.error(error);
        this.setConfidence(0.1);
      }
    },
    onLiftChange(e) {
      try {
        this.setLift(parseFloat(e.target.value));
      } catch (error) {
        console.error(error);
        this.setLift(2);
      }
    },
    onSubmit() {
      this.getRules();
      this.setSupport();
      this.setConfidence();
      this.setLift();
    },
  },
};
</script>

<style>
</style>