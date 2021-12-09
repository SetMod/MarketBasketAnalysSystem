<template>
  <div class="text-center">
    <TransactionsTable v-if="isLoaded" :transactions="transactions" />
    <TransactionsRetryButton v-else-if="!isLoaded && errorMsg" />
    <TransactionsLoading v-else />
  </div>
</template>

<script>
import { mapState } from "vuex";
import store from "../../store/index";
import TransactionsTable from "./TransactionTable.vue";
import TransactionsRetryButton from "./TransactionsRetryButton.vue";
import TransactionsLoading from "./TransactionsLoading.vue";

export default {
  name: "TransactionsList",
  store: store,
  computed: mapState(["transactions", "isLoaded", "errorMsg"]),
  methods: {
    getTransactions() {
      store.dispatch("getTransactions", {
        transactionsUrl: `${store.state.backend_url}/transactions/`,
      });
    },
  },
  components: {
    TransactionsTable,
    TransactionsRetryButton,
    TransactionsLoading,
  },
  mounted() {
    if (store.state.transactions.length == 0) {
      this.getTransactions();
    }
  },
};
</script>

<style>
</style>