from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient

# Flask app
app = Flask(__name__)
app.secret_key = "your_secret_key"

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["linkedin_profiles"]
profiles_collection = db["profiles"]

# Routes
@app.route("/")
def index():
    """Home page with a list of profiles."""
    profiles = profiles_collection.find()
    return render_template("index.html", profiles=profiles)

@app.route("/add", methods=["GET", "POST"])
def add_profile():
    """Add a new profile."""
    if request.method == "POST":
        name = request.form.get("name").strip()
        title = request.form.get("title").strip() or "N/A"
        skills = [skill.strip() for skill in request.form.get("skills").split(",") if skill.strip()]
        connections = request.form.get("connections").strip()

        if not name:
            flash("Name is required!", "error")
            return redirect(url_for("add_profile"))

        try:
            connections = int(connections) if connections else 0
        except ValueError:
            flash("Connections must be a valid number.", "error")
            return redirect(url_for("add_profile"))

        profile = {"name": name, "title": title, "skills": skills, "connections": connections}
        profiles_collection.insert_one(profile)
        flash(f"Profile for {name} added successfully!", "success")
        return redirect(url_for("index"))

    return render_template("add.html")

@app.route("/delete/<profile_id>")
def delete_profile(profile_id):
    """Delete a profile."""
    profiles_collection.delete_one({"_id": ObjectId(profile_id)})
    flash("Profile deleted successfully!", "success")
    return redirect(url_for("index"))

@app.route("/search", methods=["POST"])
def search_profile():
    """Search for a profile by name."""
    name = request.form.get("name").strip()
    if not name:
        flash("Please enter a name to search!", "error")
        return redirect(url_for("index"))

    profiles = list(profiles_collection.find({"name": {"$regex": name, "$options": "i"}}))
    if not profiles:
        flash(f"No profiles found for '{name}' on LinkedIn!", "error")
        return redirect(url_for("index"))

    return render_template("index.html", profiles=profiles)


from bson.objectid import ObjectId

@app.route("/update/<profile_id>", methods=["GET", "POST"])
def update_profile(profile_id):
    """Update an existing profile."""
    profile = profiles_collection.find_one({"_id": ObjectId(profile_id)})
    
    if not profile:
        flash("Profile not found!", "error")
        return redirect(url_for("index"))

    if request.method == "POST":
        name = request.form.get("name").strip()
        title = request.form.get("title").strip() or "N/A"
        skills = [skill.strip() for skill in request.form.get("skills").split(",") if skill.strip()]
        connections = request.form.get("connections").strip()

        try:
            connections = int(connections) if connections else 0
        except ValueError:
            flash("Connections must be a valid number.", "error")
            return redirect(url_for("update_profile", profile_id=profile_id))

        updated_profile = {
            "name": name,
            "title": title,
            "skills": skills,
            "connections": connections,
        }
        profiles_collection.update_one({"_id": ObjectId(profile_id)}, {"$set": updated_profile})
        flash(f"Profile for {name} updated successfully!", "success")
        return redirect(url_for("index"))

    return render_template("update.html", profile=profile)


if __name__ == "__main__":
    app.run(debug=True)
