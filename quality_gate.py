import json
import sys

MINIMUM_ACCURACY = 0.85


def main():
    print("Reading model evaluation metrics...")
    try:
        with open("metrics.json", "r", encoding="utf-8") as file:
            metrics = json.load(file)
        accuracy = float(metrics["accuracy"])
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"QUALITY GATE FAILED: cannot read accuracy metric: {exc}")
        return 1

    print("Model Accuracy :", round(accuracy, 4))
    print("Required Accuracy:", MINIMUM_ACCURACY)
    if accuracy < MINIMUM_ACCURACY:
        print("QUALITY GATE FAILED")
        print("Model performance is below the required threshold.")
        return 1
    print("QUALITY GATE PASSED")
    print("Model performance satisfies the required threshold.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
