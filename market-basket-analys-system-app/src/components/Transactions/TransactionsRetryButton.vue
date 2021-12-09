<template>
  <div class="mb-5">
    <div
      class="
        text-danger
        fw-bold
        border border-2
        rounded-2
        border-danger
        w-25
        m-auto
      "
    >
      {{ errorMsg }}
    </div>
    <div>
      <button
        type="button"
        class="btn btn-dark mt-3"
        v-on:click="getTransactions"
      >
        Retry
      </button>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import store from "../../store/index";
export default {
  name: "TransactionsRetryButton",
  computed: mapState(["errorMsg"]),
  methods: {
    getTransactions() {
      store.dispatch("getTransactions", {
        transactionsUrl: `${store.state.backend_url}/transactions/`,
      });
    },
  },
};
</script>

<style>
</style>