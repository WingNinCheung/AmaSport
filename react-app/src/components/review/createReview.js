import { NavLink, useParams, useHistory } from "react-router-dom";
import { getProducts } from "../../store/product";
import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { addReview } from "../../store/review";

function CreateReview() {
  // product id
  const { id } = useParams();
  const dispatch = useDispatch();
  const history = useHistory();

  const [rating, setRating] = useState(1);
  const [review, setReview] = useState("");
  const [validationError, setValidationError] = useState([]);

  const allProducts = useSelector((state) => Object.values(state.product));
  const sessionUser = useSelector((state) => state.session);
  const myProduct = allProducts.find((product) => product.id == id);


  // format the date object into Month-Date-Year
  let dateNow = new Date().toDateString().split(" ");
  dateNow.shift();
  dateNow = dateNow.join(" ");

  useEffect(() => {
    dispatch(getProducts());
  }, [dispatch]);

  // validation errors handling
  useEffect(() => {
    let errors = [];

    if (review.trim() === "") {
      errors.push("Review cannot be empty or all spaces");
    } else if (review.length > 250) {
      errors.push("Review cannot be more than 250 characters");
    }

    setValidationError(errors);
  }, [review]);

  const handleSubmit = (e) => {
    e.preventDefault();

    const data = {
      user_id: sessionUser.user.id,
      product_id: id,
      rating,
      review_body: review,
      created_at: dateNow,
    };

    const newReview = dispatch(addReview(data, id));
    if (newReview) {
      history.push(`/products/${id}`);
    }
  };

  return (
    <div className="createReview-container">
      {myProduct && (
        <div>
          <h2>Create Review</h2>
          <div>
            <img src={myProduct.image} alt="ball"></img>
          </div>
          <div>{myProduct.name}</div>
          <form onSubmit={handleSubmit}>
            <h3>Overall rating</h3>
            <select onChange={(e) => setRating(e.target.value)} value={rating}>
              <option>1</option>
              <option>2</option>
              <option>3</option>
              <option>4</option>
              <option>5</option>
            </select>
            <h3>Add a written review</h3>
            <ul>
              {validationError.map((error) => (
                <li key={error}>{error}</li>
              ))}
            </ul>
            <textarea
              onChange={(e) => setReview(e.target.value)}
              value={review}
            ></textarea>
            <button disabled={validationError.length}>Submit</button>
          </form>
        </div>
      )}
    </div>
  );
}

export default CreateReview;
