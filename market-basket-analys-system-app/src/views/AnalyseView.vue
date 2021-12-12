<template>
  <div class="container">
    <div class="m-auto row">
      <AnalyseForm class="col-lg-6" />
      <AnalyseImage class="col-lg-6" />
    </div>
    <h2 class="mt-3">Association Rules</h2>
    <RulesTable class="my-3" :rules="rules" />
  </div>
</template>

<script>
import AnalyseForm from "../components/Analyse/AnalyseForm.vue";
import AnalyseImage from "../components/Analyse/AnalyseImage.vue";
import RulesTable from "../components/Analyse/RulesTable.vue";
export default {
  name: "Analyse",
  components: {
    AnalyseForm,
    AnalyseImage,
    RulesTable,
  },
  data() {
    return {
      rules: [],
    };
  },
};
</script>

<style>
</style>