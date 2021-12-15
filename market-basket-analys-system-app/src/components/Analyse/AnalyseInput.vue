<template>
  <div class="mb-3">
    <label for="support1" class="form-label">{{ inputName }}</label>
    <input
      :min="min"
      :max="max"
      :type="inputType"
      :value="value"
      class="form-control"
      aria-describedby="inputName + 'threshold'"
    />
    <div id="inputName + 'Help1'" class="form-text" v-if="!helpText">
      Please specify {{ inputName }} between {{ min }} and {{ max }}.
    </div>
    <div id="inputName + 'Help2'" class="form-text" v-else>
      {{ helpText }}
    </div>
  </div>
</template>

<script>
export default {
  name: "AnalyseInput",
  props: {
    inputName: {
      type: String,
      required: true,
    },
    value: {
      required: true,
    },
    inputType: {
      type: String,
      default: "text",
    },
    min: {
      type: Number,
      default: 0.01,
    },
    max: {
      type: Number,
      default: 1,
    },
    helpText: {
      type: String,
      default: "",
    },
  },
};
</script>

<style>
</style>