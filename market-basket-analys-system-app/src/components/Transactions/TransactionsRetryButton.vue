<template>
  <button type="button" class="btn btn-dark my-3" v-on:click="getTransactions">
    Retry
  </button>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "TransactionsRetryButton",
  methods: {
    ...mapActions({
      getTransactions: "transactions/getTransactions",
    }),
  },
};
</script>

<style>
</style>