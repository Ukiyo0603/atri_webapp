import create from "zustand";

const useIoStore = create((set) => {
  return {
  "Home": {},
  "About": {},
  "Menu": {},
  "Pages": {},
  "Cart": {}
}});

export default useIoStore;
