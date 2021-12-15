<template>
  <div class="mt-3 text-center mt-5">
    <h2 class="py-3 mt-3">Transactions</h2>
    <div v-show="isLoaded">
      <TransactionPagination />
      <TransactionsTable :transactions="transactions" />
      <BackToTopButton />
    </div>
    <TransactionsRetryButton v-show="!isLoaded && errorMsg" />
    <LoadingCircle v-show="!isLoaded && !errorMsg" />
    <div class="alert alert-danger" role="alert" v-show="errMsg">
      {{ errMsg }}
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from "vuex";
import store from "../store/index";
import TransactionsTable from "../components/Transactions/TransactionsTable.vue";
import TransactionsRetryButton from "../components/Transactions/TransactionsRetryButton.vue";
import LoadingCircle from "../components/LoadingCircle.vue";
import BackToTopButton from "../components/BackToTopButton.vue";
import TransactionPagination from "../components/Transactions/TransactionPagination.vue";

export default {
  name: "Transactions",
  components: {
    TransactionsTable,
    TransactionsRetryButton,
    LoadingCircle,
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
    if (this.transactions.length === 0) {
      this.getTransactions();
    }
  },
};
</script>

<style>
</style>