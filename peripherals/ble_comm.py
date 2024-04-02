import asyncio
from bleak import BleakScanner, BleakClient, BleakGATTCharacteristic

address = "44:27:F3:4B:98:71"
MODEL_NBR_UUID = "2A24"


async def main():
    devices = await BleakScanner.discover(return_adv=True)
    for d in devices:
        print(d)
        print(devices[d])
        print()

    async with BleakClient(address) as client:
        model_number = await client.read_gatt_char(BleakGATTCharacteristic.uuid)
        print("Model Number: {0}".format("".join(map(chr, model_number))))


if __name__ == "__main__":
    asyncio.run(main())


