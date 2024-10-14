object Main {
  def main(args: Array[String]): Unit = {
    val store = new KeyValueStore

    // Add some key-value pairs
    store.put("name", "Alice")
    store.put("age", "30")
    store.put("city", "New York")

    // Retrieve and print values
    println(s"Name: ${store.get("name").getOrElse("Not found")}")
    println(s"Age: ${store.get("age").getOrElse("Not found")}")
    println(s"City: ${store.get("city").getOrElse("Not found")}")

    // Remove a key-value pair
    store.remove("age")

    // Try to retrieve the removed value
    println(s"Age after removal: ${store.get("age").getOrElse("Not found")}")

    // Print all keys
    println(s"All keys: ${store.keys().mkString(", ")}")
  }
}

class KeyValueStore {
  private var store: Map[String, String] = Map()

  def put(key: String, value: String): Unit = {
    store = store + (key -> value) // Add or update the value associated with the key
  }

  def get(key: String): Option[String] = {
    store.get(key) // Retrieve the value, or None if it doesn't exist
  }

  def remove(key: String): Unit = {
    store = store - key // Remove the key-value pair
  }

  def keys(): List[String] = {
    store.keys.toList // Return a list of all keys
  }
}



