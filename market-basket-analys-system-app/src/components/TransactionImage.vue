<template>
  <div>
    <img v-bind:src="imageUrl" class="img-fluid" alt="Transactions per month" />
  </div>
</template>

<script>
import store from "../store/index";
export default {
  name: "TransactionImage",
  store: store,
  computed: {
    imageUrl() {
      return `${store.state.backend_url}/transactions/images/transactions_by_month.png`;
    },
  },
};
</script>

<style>
</style>