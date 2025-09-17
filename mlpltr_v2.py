import os
import numpy as np 


def read_data(input_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File {input_file} not found")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Extract array names (5th line)
    array_names = lines[4].strip().split()

    # Extract data (starting from 7th line)
    data = []
    for line in lines[6:]:
        if line.strip():
            # Check for duplicate column headers
            if any(name in line for name in array_names):
                continue
            data.append(list(map(float, line.strip().split())))

    # Convert to NumPy array
    data_array = np.array(data)

    # Create dictionary mapping array names to columns
    arrays = {name: data_array[:, i] for i, name in enumerate(array_names)}

    # # Time filtering
    # mask = time > 0

    return arrays

def overshoot(signal):
    steady_state_value = signal[-1]
    peak_value = np.max(signal)
    overshoot_value = (peak_value - steady_state_value) / steady_state_value
    return overshoot_value

def settling_time(time, signal, threshold=0.005):
    steady_state_value = signal[-1]
    upper_bound = steady_state_value * (1 + threshold)
    lower_bound = steady_state_value * (1 - threshold)

    for i in range(len(signal)-1, -1, -1):
        if signal[i] > upper_bound or signal[i] < lower_bound:
            return time[i+1] if i+1 < len(time) else time[-1]
    return time[0]

def undershoot(signal):
    steady_state_value = signal[-1]
    trough_value = np.min(signal)
    undershoot_value = (steady_state_value - trough_value) / steady_state_value
    return undershoot_value


def main():
    folder = '5_decrease'
    powers = [40, 50, 60, 70, 80, 90, 100]
    gains = (0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.25, 1.5, 1.75)
    for power in powers:
        for gain in gains:
            input_file = os.path.join(folder, f'results_{power}_{gain}.plt')
            arrays = read_data(input_file)
            signal = arrays['GROUT(34)']
            overshoot_value = overshoot(signal)
            time = arrays['TIME']
            settling_time_value = settling_time(time-1000, signal)
            # print(f"Overshoot: {overshoot_value*100:.2f}%")
            print(power,'    ', gain,'    ',f"{settling_time_value:.2f} seconds")


if __name__ == "__main__":
    main()
