from typing import List, Dict, Any


def hello_world() -> str:
    """
    Una función simple que devuelve un saludo.
    
    Returns:
        str: Un mensaje de saludo
    """
    return "¡Hola, mundo!"


def process_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Procesa una lista de diccionarios.
    
    Args:
        data: Lista de diccionarios a procesar
        
    Returns:
        Lista procesada de diccionarios
    """
    return [item for item in data if "active" in item and item["active"]]


def main() -> None:
    """Función principal del programa."""
    message = hello_world()
    print(message)
    
    # Ejemplo de uso de tipado
    sample_data: List[Dict[str, Any]] = [
        {"id": 1, "name": "Item 1", "active": True},
        {"id": 2, "name": "Item 2", "active": False},
        {"id": 3, "name": "Item 3", "active": True},
    ]
    
    processed = process_data(sample_data)
    print(f"Datos procesados: {processed}")


if __name__ == "__main__":
    main() 