import { shallowMount } from '@vue/test-utils';
import ProductOverview from '@/components/ProductOverview.vue';

describe('ProductOverview', () => {
  it('displays a list of products', () => {
    const wrapper = shallowMount(ProductOverview, {
      data() {
        return {
          products: [
            { id: 1, name: 'Product 1', description: 'Description 1', price: 9.99 },
            { id: 2, name: 'Product 2', description: 'Description 2', price: 19.99 },
          ],
        };
      },
    });
    expect(wrapper.findAll('.product-card')).toHaveLength(2);
  });

  it('filters products based on search query', () => {
    const wrapper = shallowMount(ProductOverview, {
      data() {
        return {
          products: [
            { id: 1, name: 'Product 1', description: 'Description 1', price: 9.99 },
            { id: 2, name: 'Product 2', description: 'Description 2', price: 19.99 },
            { id: 3, name: 'Product 3', description: 'Description 3', price: 29.99 },
          ],
        };
      },
    });
    const searchInput = wrapper.find('input[type="text"]');
    searchInput.setValue('Product 2');
    expect(wrapper.findAll('.product-card')).toHaveLength(1);
    expect(wrapper.text()).toContain('Product 2');
  });
});
