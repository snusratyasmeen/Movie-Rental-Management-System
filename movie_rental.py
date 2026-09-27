print("🎬 Movie Rental Management System")

movies = []

while True:
    print("\n1. Add Movie")
    print("2. View Movies")
    print("3. Search Movie")
    print("4. Update Rental Status")
    print("5. Delete Movie")
    print("6. Count Movies")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # Add Movie
    if choice == "1":
        movie_id = input("Enter movie ID: ")
        title = input("Enter movie title: ")
        genre = input("Enter genre: ")
        year = input("Enter release year: ")

        movie = {
            "id": movie_id,
            "title": title,
            "genre": genre,
            "year": year,
            "status": "Available"
        }

        movies.append(movie)

        print("✅ Movie added successfully!")

    # View Movies
    elif choice == "2":
        if len(movies) == 0:
            print("❌ No movies found.")
        else:
            print("\n🎬 Movie Details")
            print("--------------------------")

            for movie in movies:
                print("Movie ID:", movie["id"])
                print("Movie Title:", movie["title"])
                print("Genre:", movie["genre"])
                print("Release Year:", movie["year"])
                print("Status:", movie["status"])
                print("--------------------------")

    # Search Movie
    elif choice == "3":
        search_id = input("Enter movie ID to search: ")

        found = False

        for movie in movies:
            if movie["id"] == search_id:
                print("\n✅ Movie Found")
                print("Movie ID:", movie["id"])
                print("Movie Title:", movie["title"])
                print("Genre:", movie["genre"])
                print("Release Year:", movie["year"])
                print("Status:", movie["status"])

                found = True
                break

        if not found:
            print("❌ Movie not found.")

    # Update Rental Status
    elif choice == "4":
        update_id = input("Enter movie ID: ")

        found = False

        for movie in movies:
            if movie["id"] == update_id:

                print("\n1. Available")
                print("2. Rented")

                status_choice = input("Choose rental status: ")

                if status_choice == "1":
                    movie["status"] = "Available"
                elif status_choice == "2":
                    movie["status"] = "Rented"
                else:
                    print("❌ Invalid status!")
                    break

                print("✅ Rental status updated successfully!")
                found = True
                break

        if not found:
            print("❌ Movie not found.")

    # Delete Movie
    elif choice == "5":
        delete_id = input("Enter movie ID to delete: ")

        found = False

        for movie in movies:
            if movie["id"] == delete_id:
                movies.remove(movie)

                print("✅ Movie deleted successfully!")
                found = True
                break

        if not found:
            print("❌ Movie not found.")

    # Count Movies
    elif choice == "6":
        print("🎬 Total Movies:", len(movies))

    # Exit
    elif choice == "7":
        print("Thank you for using Movie Rental Management System! 🎬")
        break

    else:
        print("❌ Invalid choice!")
