<template>
  <div class="transactions mt-3">
    <div class="container row">
      <TransactionsForm class="col-lg-6" />
      <TransactionImage class="col-lg-6" />
    </div>
    <TransactionsList />
  </div>
</template>

<script>
import TransactionsList from "../components/TransactionsList.vue";
import TransactionsForm from "../components/TransactionsForm.vue";
import TransactionImage from "../components/TransactionImage.vue";

export default {
  name: "Transactions",
  components: {
    TransactionsList,
    TransactionsForm,
    TransactionImage,
  },
};
</script>

<style>
.transactions {
  font-size: 20px;
}
</style>