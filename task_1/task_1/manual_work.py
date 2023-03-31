from db_interface import DbInterface
import argparse

if __name__ == '__main__':
    db_iface = DbInterface()
    parser = argparse.ArgumentParser()
    parser.add_argument('--key')
    parser.add_argument('--value')
    args_namespace = parser.parse_args()
    
    if args_namespace.key and args_namespace.value:
        db_iface.set_val(args_namespace.key, args_namespace.value)
    elif args_namespace.key:
        try:
            print(', '.join(db_iface.get_val(args_namespace.key)))
        except Exception as e:
            print(e)
