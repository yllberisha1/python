from fastapi import APIRouter, HTTPException
from typing import List, Optional
from models.recipe import Recipe, RecipeCreate
from database import get_db_connection

router = APIRouter()


def category_exists(category_id: int) -> bool:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM categories WHERE id = ?", (category_id,))
    result = cursor.fetchone()
    conn.close()
    return result is not None


@router.get("/recipes/", response_model=List[Recipe])
def get_recipes(cuisine: Optional[str] = None, difficulty: Optional[str] = None):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM recipes WHERE 1=1"
    params = []

    if cuisine:
        query += " AND cuisine = ?"
        params.append(cuisine)

    if difficulty:
        query += " AND difficulty = ?"
        params.append(difficulty)

    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()

    return [
        Recipe(
            id=row[0],
            name=row[1],
            description=row[2],
            ingredients=row[3],
            instructions=row[4],
            cuisine=row[5],
            difficulty=row[6],
            category_id=row[7],
        )
        for row in rows
    ]


@router.post("/recipes/", response_model=Recipe)
def create_recipe(recipe: RecipeCreate):
    if not category_exists(recipe.category_id):
        raise HTTPException(status_code=400, detail="Category does not exist")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO recipes (name, description, ingredients, instructions, cuisine, difficulty, category_id) VALUES (?,?,?,?,?,?,?)",
        (recipe.name, recipe.description, recipe.ingredients, recipe.instructions, recipe.cuisine, recipe.difficulty, recipe.category_id)
    )
    conn.commit()
    recipe_id = cursor.lastrowid
    conn.close()
    return Recipe(
        id=recipe_id,
        name=recipe.name,
        description=recipe.description,
        ingredients=recipe.ingredients,
        instructions=recipe.instructions,
        cuisine=recipe.cuisine,
        difficulty=recipe.difficulty,
        category_id=recipe.category_id
    )


@router.put("/recipe/{recipe_id}", response_model=Recipe)
def update_recipe(recipe_id: int, recipe: RecipeCreate):
    if not category_exists(recipe.category_id):
        raise HTTPException(status_code=400, detail="Category does not exist")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE recipes SET name=?, description=?, ingredients=?, instructions=?, cuisine=?, difficulty=?, category_id=? WHERE id=?",
        (
            recipe.name,
            recipe.description,
            recipe.ingredients,
            recipe.instructions,
            recipe.cuisine,
            recipe.difficulty,
            recipe.category_id,
            recipe_id
        )
    )

    cursor.execute("SELECT * FROM recipes WHERE id = ?", (recipe_id,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Recipe not found")

    return Recipe(
        id=row[0],
        name=row[1],
        description=row[2],
        ingredients=row[3],
        instructions=row[4],
        cuisine=row[5],
        difficulty=row[6],
        category_id=row[7]
    )


@router.delete("/recipes/{recipe_id}", response_model=dict)
def delete_recipe(recipe_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recipes WHERE id = ?", (recipe_id,))
    recipe = cursor.fetchone()
    if recipe is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Recipe not found")
    cursor.execute("DELETE FROM recipes WHERE id = ?", (recipe_id,))
    conn.commit()
    conn.close()

    return {"message": f"Recipe with ID {recipe_id} has been deleted."}
