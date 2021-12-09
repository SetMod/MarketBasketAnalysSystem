<template>
  <form class="row g-3">
    <div class="col">
      <TransactionInput inputName="Support" />
      <TransactionInput inputName="Confidence" />
      <TransactionInput inputName="Lift" />
    </div>

    <div class="mb-3 form-check">
      <input type="checkbox" class="form-check-input" id="exampleCheck1" />
      <label class="form-check-label" for="exampleCheck1">Check me out</label>
    </div>

    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
</template>

<script>
import TransactionInput from "./TransactionInput.vue";
export default {
  name: "TransactionForm",
  data() {
    return {
      support: 0.01,
    };
  },
  methods: {
    onSupportInput() {
      console.log(this.support);
      console.log(this);
    },
  },
  components: {
    TransactionInput,
  },
};
</script>

<style>
</style>