#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

// Função para importar e converter CSV
void import_and_convert_csv(const std::string& csv_file, std::vector<double>& xs, std::vector<double>& ys, std::vector<double>& zs) {
    std::ifstream file(csv_file);
    std::string line;
    std::getline(file, line); // Ignorar a primeira linha (cabeçalho)

    while (std::getline(file, line)) {
        std::stringstream ss(line);
        std::string item;
        std::getline(ss, item, ',');
        xs.push_back(std::stod(item));
        std::getline(ss, item, ',');
        ys.push_back(std::stod(item));
        std::getline(ss, item, ',');
        zs.push_back(std::stod(item));
    }
}

// Função principal
int main() {
    std::vector<std::string> file_names = {
        "calibration_sensor_Port.S1_Color.BLUE_2020_04_11_02_38_00_002935.csv",
        "calibration_sensor_Port.S1_Color.BROWN_2020_04_11_02_39_22_229294.csv",
        "calibration_sensor_Port.S1_Color.BLACK_2020_04_11_02_39_39_117926.csv",
        "calibration_sensor_Port.S1_Color.GREEN_2020_04_11_02_39_05_486703.csv",
        "calibration_sensor_Port.S1_Color.RED_2020_04_11_02_38_48_567920.csv",
        "calibration_sensor_Port.S1_Color.WHITE_2020_04_11_02_40_17_819093.csv",
        "calibration_sensor_Port.S1_Color.YELLOW_2020_04_11_02_39_57_169476.csv"
    };

    std::vector<std::string> color_names = {"blue", "brown", "black", "green", "red", "white", "yellow"};

    for (size_t i = 0; i < file_names.size(); ++i) {
        std::vector<double> xs, ys, zs;
        import_and_convert_csv(file_names[i], xs, ys, zs);

        std::ofstream output_file("data_" + color_names[i] + ".dat");
        for (size_t j = 0; j < xs.size(); ++j) {
            output_file << xs[j] << " " << ys[j] << " " << zs[j] << "\n";
        }
        output_file.close();
    }

    return 0;
}

