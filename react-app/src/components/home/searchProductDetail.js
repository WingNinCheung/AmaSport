import { useDispatch, useSelector } from "react-redux";
import { useEffect } from "react";
import { getProducts } from "../../store/product";
import { NavLink, useParams } from "react-router-dom";

function SearchProductDetail() {
  const dispatch = useDispatch();
  const allProducts = useSelector((state) => Object.values(state.product));
  const { category, text } = useParams();
  let searchProduct;

  console.log("this", category, text);

  console.log("all products", allProducts);

  if (category === "All") {
    searchProduct = allProducts.filter((product) => {
      return product.name.toLowerCase().includes(text.toLowerCase());
    });
  } else {
    searchProduct = allProducts.filter((product) => {
      return (
        product.name.toLowerCase().includes(text.toLowerCase()) &&
        product.category.toLowerCase() === category.toLowerCase()
      );
    });
  }

  console.log("search result ,", searchProduct);

  useEffect(() => {
    dispatch(getProducts());
  }, [dispatch]);

  return (
    <div>
      {searchProduct &&
        searchProduct.map((product) => (
          <div key={product.id}>
            <NavLink to={`/products/${product.id}`}>
              <img src={product.image} alt="products"></img>
              <div>{product.name}</div>
            </NavLink>
            <div>${product.price}</div>
            <div>Get it by {product.date_available}</div>
            <div>FREE Shipping by {product.manufacturer}</div>
          </div>
        ))}
      {!searchProduct.length && (
        <div>
          <h3>Sorry. No products found matching your search...</h3>
        </div>
      )}
    </div>
  );
}

export default SearchProductDetail;
