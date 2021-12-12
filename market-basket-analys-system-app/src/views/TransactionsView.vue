<template>
  <div class="mt-3 text-center mt-5">
    <h2 class="py-3 mt-3">Transactions</h2>
    <div v-if="isLoaded">
      <TransactionPagination />
      <TransactionsTable :transactions="transactions" />
      <BackToTopButton />
    </div>
    <TransactionsRetryButton v-else-if="!isLoaded && errorMsg" />
    <TransactionsLoading v-else />
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from "vuex";
import store from "../store/index";
import TransactionsTable from "../components/Transactions/TransactionsTable.vue";
import TransactionsRetryButton from "../components/Transactions/TransactionsRetryButton.vue";
import TransactionsLoading from "../components/Transactions/TransactionsLoading.vue";
import BackToTopButton from "../components/BackToTopButton.vue";
import TransactionPagination from "../components/Transactions/TransactionPagination.vue";

export default {
  name: "Transactions",
  components: {
    TransactionsTable,
    TransactionsRetryButton,
    TransactionsLoading,
    BackToTopButton,
    TransactionPagination,
  },
  store: store,
  computed: {
    ...mapState({
      transactions: (state) => state.transactions.transactions,
      isLoaded: (state) => state.transactions.isLoaded,
      errorMsg: (state) => state.transactions.errorMsg,
    }),
    ...mapGetters({}),
  },
  methods: {
    ...mapActions({
      getTransactions: "transactions/getTransactions",
      getNextPage: "transactions/getNextPage",
      getPreviousPage: "transactions/getPreviousPage",
    }),
  },
  mounted() {
    if (store.state.transactions.transactions.length == 0) {
      this.getTransactions();
    }
  },
};
</script>

<style>
</style>