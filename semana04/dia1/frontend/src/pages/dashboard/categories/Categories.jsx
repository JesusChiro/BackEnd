import { useContext, useEffect, useState } from "react";
import { FaTrashAlt } from "react-icons/fa";
import { AdminContext } from "../../../contexts/AdminContext";
import { getToken } from "../../../services/authServices";
import { deleteCategoryService,getAllCategoriesService, postCategoryService} from "../../../services/CategoriesServices";
import "./Categories.scss";

export const Categories = () => {
  const { setAdminTitle } = useContext(AdminContext);
  const [listOfCategories, setListOfCategories] = useState([]);
  const [category, setCategory] = useState({
    name: "",
  });
  const [bandera, setBandera] = useState(false);

  useEffect(() => {
    setAdminTitle("Categories");
    const fetchData = async () => {
      const token = getToken();
      const response = await getAllCategoriesService(token);
      console.log(response.data.content)
   
        setListOfCategories(response.data.content);
      
    };
    fetchData();
  }, [bandera]);

  const createCategory = async (event) => {
    event.preventDefault();
    try {
      // const token = getToken();
      const response = await postCategoryService(category);
      console.log(response)
      if (response.status === 201) {
        setBandera(!bandera);
        setCategory({
          nombre: "",
        });
      } else {
        throw new Error(response.message);
      }
    } catch (error) {
      console.log(error.message);
    }
  };

  const deleteCategory = async (category_id) => {
    try {
      // const token = getToken();
      const response = await deleteCategoryService(category_id);
      if (response.status === 200) {
        setBandera(!bandera);
      } else {
        throw new Error(response.message);
      }
    } catch (error) {
      console.log(error.message);
    }
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    return setCategory({ ...category, [name]: value });
  };

  return (
    <div className="Products">
      <h4 className="Products-subtitle">All categories</h4>
      <div className="Products-table">
        <table>
          <thead>
            <tr>
              <th>#</th>
              <th>Category name</th>
              <th>Options</th>
            </tr>
          </thead>
          <tbody>
            {listOfCategories.length > 0 &&
              listOfCategories.map((category) => (
                <tr key={category.id}>
                  {/* <td>{index + 1}</td> */}
                  <td>{category.name}</td>
                  <td>
                    <FaTrashAlt onClick={() => deleteCategory(category.id)} />
                  </td>
                </tr>
              ))}
          </tbody>
        </table>
      </div>

      <h4 className="Products-subtitle">Create category</h4>
      <form className="Products-create-form" onSubmit={createCategory}>
        <div className="form-group">
          <label htmlFor="nombre">Category name</label>
          <input
            type="text"
            name="name"
            id="name"
            value={category.name}
            onChange={handleInputChange}
          />
        </div>
        <div className="form-group">
          <button type="submit" className="Products-create-button">
            Create category
          </button>
        </div>
      </form>
    </div>
  );
};
