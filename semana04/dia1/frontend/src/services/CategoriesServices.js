import { API_URL } from "@lib/Enviroments";

export const getAllCategoriesService = async (token) => {
  const response = await fetch(`${API_URL}/category`, {
    headers: {
      Authorization: "Bearer " + token,
    },
  });
  const status = response.status;
  const data = await response.json();
  return { data, status };
};

export const postCategoryService = async (category) => {
  const response = await fetch(`${API_URL}/categorias/crear`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      // Authorization: `Bearer ${token}`,
    },
    body: JSON.stringify(category),
  });
  const status = response.status;
  const data = await response.json();
  return { data, status };
};

export const deleteCategoryService = async (id) => {
  const response = await fetch(`${API_URL}/categorias/eliminar/${id}`, {
    method: "DELETE",
    headers: {
      // Authorization: "Bearer " + token,
    },
  });
  const status = response.status;
  const data = await response.json();
  return { data, status };
};
