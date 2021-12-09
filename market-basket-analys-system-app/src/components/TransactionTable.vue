<template>
  <div>
    <div class="py-3 fw-bold fs-3">Transactions</div>
    <table class="table table-striped">
      <thead>
        <tr>
          <th scope="col">CostPerItem</th>
          <th scope="col">Country</th>
          <th scope="col">ItemCode</th>
          <th scope="col">ItemDescription</th>
          <th scope="col">NumberOfItemsPurchased</th>
          <th scope="col">TransactionId</th>
          <th scope="col">TransactionTime</th>
          <th scope="col">UserId</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(transaction, key1) in transactions" :key="key1">
          <th v-for="(val, key2) in transaction" :key="key2">{{ val }}</th>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "TransactonsTable",
  props: {
    transactions: {
      type: Array,
      required: true,
    },
  },
};
</script>

<style>
</style>