def create_flight(flight_number, destination, capacity):
    return {
        'flight_number': flight_number,
        'destination': destination,
        'capacity': capacity,
        'passengers': []
    }

def available_seats(flight):
    return flight['capacity'] - len(flight['passengers'])

def book_seat(flight, passenger_name):
    if available_seats(flight) > 0:
        flight['passengers'].append(passenger_name)
        print(f"Reserva confirmada para {passenger_name} no voo {flight['flight_number']}.")
    else:
        print(f"Desculpe, não há assentos disponíveis no voo {flight['flight_number']}.")

def display_flights(flights):
    print("Voos disponíveis:")
    for i, flight in enumerate(flights, start=1):
        print(f"{i}. Voo {flight['flight_number']}: Destino - {flight['destination']}, Assentos disponíveis - {available_seats(flight)}")

def main():
    # Exemplo de criação de voos
    flights = [
        create_flight("AA123", "Nova York", 100),
        create_flight("BB456", "Los Angeles", 150),
        create_flight("CC789", "Chicago", 120)
    ]

    while True:
        print("\nBem-vindo ao Sistema de Reserva de Passagens Aéreas")
        display_flights(flights)

        choice = input("\nEscolha um voo (ou 'q' para sair): ")
        if choice.lower() == 'q':
            break

        try:
            flight_number = int(choice)
            selected_flight = flights[flight_number - 1]

            passenger_name = input("Digite seu nome: ")
            book_seat(selected_flight, passenger_name)

        except (ValueError, IndexError):
            print("Escolha inválida. Por favor, digite o número do voo.")

if __name__ == "__main__":
    main()
