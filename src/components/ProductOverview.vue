<template>
  <div>
    <h1>Product Overview</h1>
    <div class="search-bar">
      <input type="text" v-model="searchQuery" placeholder="Search products..." />
    </div>
    <div class="product-list">
      <div class="product-card" v-for="product in filteredProducts" :key="product.id">
        <h3>{{ product.name }}</h3>
        <p>{{ product.description }}</p>
        <p>Price: {{ product.price }}</p>
      </div>
      <p v-if="filteredProducts.length === 0">No products found.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '',
      products: [],
    };
  },
  computed: {
    filteredProducts() {
      return this.products.filter((product) =>
        product.name.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    },
  },
  mounted() {
    this.fetchProducts();
  },
  methods: {
    async fetchProducts() {
      try {
        const response = await fetch('/api/products');
        this.products = await response.json();
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    },
  },
};
</script>

<style scoped>
.search-bar {
  margin-bottom: 1rem;
}
.product-list {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  grid-gap: 1rem;
}
.product-card {
  border: 1px solid #ccc;
  padding: 1rem;
}
</style>
