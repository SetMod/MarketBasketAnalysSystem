<template>
  <form class="row g-3">
    <div class="col">
      <AnalyseInput inputName="Support" @input="inputSupport" />
      <AnalyseInput inputName="Confidence" v-model="confidence" />
      <AnalyseInput inputName="Lift" v-model="lift" />
    </div>

    <div class="mb-3 form-check">
      <input type="checkbox" class="form-check-input" id="exampleCheck1" />
      <label class="form-check-label" for="exampleCheck1">Check me out</label>
    </div>

    <button type="submit" class="btn btn-primary" @click="onSupportInput">
      Submit
    </button>
  </form>
</template>

<script>
import AnalyseInput from "./AnalyseInput.vue";
export default {
  name: "AnalyseForm",
  data() {
    return {
      support: 0.01,
      confidence: 0.01,
      lift: 0.01,
    };
  },
  methods: {
    inputSupport(e) {
      try {
        this.support = parseFloat(e.target.value);
      } catch (error) {
        console.error(error);
        this.support = 0.01;
      }
    },
    onSupportInput(e) {
      e.preventDefault();
      console.log(this.support);
      console.log(this.confidence);
      console.log(this.lift);
    },
  },
  components: {
    AnalyseInput,
  },
};
</script>

<style>
</style>