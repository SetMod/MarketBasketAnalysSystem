<template>
  <div class="container">
    <div class="m-auto row">
      <AnalyseForm class="col-lg-6" />
      <AnalyseImage class="col-lg-6" />
    </div>
    <h2 class="mt-3">Association Rules</h2>
    <div v-show="isLoaded">
      <RulesTable class="my-3" :rules="rules" />
      <BackToTopButton />
    </div>
    <LoadingCircle v-show="!errMsg && !isLoaded" class="text-center" />
    <div class="alert alert-danger" role="alert" v-show="errMsg">
      {{ errMsg }}
    </div>
  </div>
</template>

<script>
import store from "../store/index";
import { mapActions, mapState } from "vuex";
import AnalyseForm from "../components/Analyse/AnalyseForm.vue";
import AnalyseImage from "../components/Analyse/AnalyseImage.vue";
import RulesTable from "../components/Analyse/RulesTable.vue";
import BackToTopButton from "../components/BackToTopButton.vue";
import LoadingCircle from "../components/LoadingCircle.vue";
export default {
  name: "Analyse",
  components: {
    BackToTopButton,
    LoadingCircle,
    AnalyseForm,
    AnalyseImage,
    RulesTable,
  },
  store,
  computed: {
    ...mapState({
      rules: (state) => state.analyse.rules,
      isLoaded: (state) => state.analyse.isLoaded,
      errMsg: (state) => state.analyse.errMsg,
    }),
  },
  methods: {
    ...mapActions({
      getRules: "analyse/getRules",
    }),
  },
  mounted() {
    if (this.rules.length == 0) {
      this.getRules();
    }
  },
};
</script>

<style>
</style>