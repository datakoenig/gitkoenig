section Section1;
shared DF_load_01_Increment_Datenbasis = let
  Source = PowerPlatform.Dataflows([]),
  #"Navigation 1" = Source{[Id = "Workspaces"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[workspaceId = "c2e1c5a3-3373-4485-8226-5b428f0efd89"]}[Data],
  #"Navigation 3" = #"Navigation 2"{[dataflowId = "234c1f3e-e1f5-466c-8084-87d77519e055"]}[Data],
  Navigation = #"Navigation 3"{[entity = "datenbasis_expand", version = ""]}[Data],
  #"Filtered rows" = Table.SelectRows(Navigation, each [Bundesland] = " Berlin")
in
  #"Filtered rows";
