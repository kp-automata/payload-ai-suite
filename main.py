"""CLI entry point for tools access.
"""
import argparse
import model

if __name__ == "__main__":
    parser  = argparse.ArgumentParser(
    prog='Payload AI Software Suite',
    description='Remote sensing mission core tools for wildfire image classficiation and training data retrieval'
    )
    # VGG16 and ResNet50 supported for now
    parser.add_argument('-r', '--run-model', required=False, type=bool)

    args = parser.parse_args()
    if args.run_model:
        model.run()
    else:
        print("No args sent to CLI")



