<template>
  <div>Transactions</div>
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
    <tbody v-for="(transaction, key1) in transactions" :key="key1">
      <tr v-for="(val, key2) in transaction" :key="key2">
        <th>{{ val }}</th>
      </tr>
    </tbody>
  </table>

  <!-- <button
    class="btn btn-primary"
    data-bs-target="#collapseTarget"
    data-bs-toggle="collapse"
  >
    Bootstrap collapse
  </button>
  <div class="collapse py-2" id="collapseTarget">
    This is the toggle-able content!
  </div> -->
</template>

<script>
import axios from "axios";

export default {
  name: "TransactionsList",
  data() {
    return {
      transactions: [],
      backend_path: "http://127.0.0.1:3000/transactions/",
    };
  },
  methods: {
    getTransactions() {
      axios
        .get(this.backend_path)
        .then((res) => {
          this.transactions = res.data;
          console.log(this);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  mounted() {
    this.getTransactions();
  },
};
</script>

<style>
</style>